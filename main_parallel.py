import os

import click
from minheap import MinHeap
import time
# import multiprocessing as mp
import multiprocess as mp

cores = 4
pool = mp.Pool(cores)
heaps = [MinHeap(10) for _ in range(cores)]
jobs = []


def process_wrapper(chunkStart, heap, max_row):
    f = open("data.csv", 'rb')
    f.seek(chunkStart)
    row_count = 0
    while row_count < max_row:
        line = f.readline()
        if not line:
            return
        row = str(line).split(",")
        heap.add(int(row[1][:-3]), row[0])


@click.command()
@click.option('--file_path', help='File path')
@click.option('--n', default=10, help='Top n values to get uuid')
def get_top_n(file_path, n):
    start = time.time()

    # init objects

    def chunkify(f, fileEnd, size=1024 * 1024):
        chunkEnd = f.tell()
        while True:
            chunkStart = chunkEnd
            f.seek(size, 1)
            f.readline()
            chunkEnd = f.tell()
            yield chunkStart, chunkEnd - chunkStart
            if chunkEnd > fileEnd:
                break

    row_number = 0
    fileEnd = os.path.getsize(file_path)

    jobs = []
    f = open("data.csv", 'rb')
    for chunkStart, chunkSize in chunkify(f, fileEnd, size=fileEnd // 4):
        jobs.append((chunkStart, heaps[row_number], ((5000000 // 4) * row_number + 1),))
        row_number += 1
    pool.starmap(process_wrapper, jobs)

    print("DONE")
    print(heaps[0])
    # wait for all jobs to finish
    heap = heaps[0]
    for h in heaps[1:]:
        print(h)
        print("Done, combining")
        heap.combine(h)

    occurrences = heap.elements.print_values()

    print("============================================================")
    print(f"Top {n} values  : {heap}")
    print(f"Total rows      : {row_number}")
    print(f"Matched rows    : {occurrences}")
    print(f"Matched percent : {100 * occurrences / row_number} %")
    print(f"Time took       : {time.time() - start} seconds")
    print("============================================================")
    return True


if __name__ == '__main__':
    get_top_n()
