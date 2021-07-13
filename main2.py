import click
from minheap import MinHeap
import time


@click.command()
@click.option('--file_path', help='File path')
@click.option('--n', default=10, help='Top n values to get uuid')
def get_top_n(file_path, n):
    start = time.time()
    data = open(file_path, "r")
    heap = MinHeap(n)

    row_count = 0
    while True:
        line = data.readline()
        if not line:
            break
        row = line.split(",")
        heap.add(int(row[1]), row[0])
        row_count += 1

    occurrences = heap.elements.print_values()

    print("============================================================")
    print(f"Top {n} values  : {heap}")
    print(f"Total rows      : {row_count}")
    print(f"Matched rows    : {occurrences}")
    print(f"Matched percent : {100 * occurrences / row_count} %")
    print(f"Time took       : {time.time() - start} seconds")
    print("============================================================")
    return True


if __name__ == '__main__':
    get_top_n()
