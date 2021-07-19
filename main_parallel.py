import os

import click
from minheap import MinHeap
import time
# import multiprocessing as mp
import multiprocess as mp

cores = 4
pool = mp.Pool(cores)


def process_wrapper(chunk_start, chunk_end, n, f):
    heap = MinHeap(n)
    f.seek(chunk_start)

    line = "START"
    if chunk_start != 0:
        line = f.readline()  # Discard the partial line

    while line and line != '' and f.tell() < chunk_end:
        line = f.readline()
        row = str(line).split(",")
        val = int(row[1][:-3])
        heap.add(val, row[0])

    return heap


@click.command()
@click.option('--file_path', help='File path')
@click.option('--n', default=10, help='Top n values to get uuid')
def get_top_n(file_path, n):
    start = time.time()

    # init objects
    size = os.path.getsize(file_path)
    chunk_size = size // cores

    with open(file_path, 'rb') as f:
        jobs = [(i * chunk_size, (i + 1) * chunk_size, n, f) for i in range(cores)]
        heaps = pool.starmap(process_wrapper, jobs)

    # wait for all jobs to finish
    heap = heaps[0]
    for h in heaps[1:]:
        heap.combine(h)

    occurrences = heap.elements.print_values()
    row_number = heap.counter

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
