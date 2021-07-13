import click
import time
import random
import uuid


@click.command()
@click.option('--file_path', help='File path')
@click.option('--count', default=1000, help='Number of rows.')
def gen_data(count, file_path):
    start = time.time()
    f = open(file_path, "w")
    for i in range(count):
        f.write(f"{uuid.uuid4()},{random.randint(0, count)}\n")

    print(f"File created at : {file_path}")
    print(f"Time took       : {time.time() - start} seconds")


if __name__ == '__main__':
    gen_data()
