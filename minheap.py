import sys


class MinHeap:

    def __init__(self, maxsize):
        self.name = "test"
        self.size = 0
        self.maxsize = maxsize
        self.Heap = [sys.maxsize] * (maxsize + 1)
        self.Heap[0] = -sys.maxsize
        self.top = 1
        self.elements = set()

    def parent(self, pos):
        return pos // 2

    def swap(self, pos1, pos2):
        self.Heap[pos1], self.Heap[pos2] = self.Heap[pos2], self.Heap[pos1]

    def add(self, element):
        if element in self.elements or (element < self.Heap[1] and self.size == self.maxsize):
            return

        if self.size == self.maxsize:
            self.pop()

        self.size += 1
        self.Heap[self.size] = element

        current = self.size
        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

        self.elements.add(element)

    def isNotCorrectNode(self, current):
        has_left_child = self.get_left_child(current) is not None and self.Heap[current] > self.Heap[
            self.get_left_child(current)]

        has_right_child = self.get_right_child(current) is not None and self.Heap[current] > self.Heap[
            self.get_right_child(current)]

        return has_left_child or has_right_child

    def pop(self):
        return_value = self.Heap[1]
        self.swap(1, self.size)
        self.Heap[self.size] = sys.maxsize
        self.size -= 1

        current = 1
        while self.isNotCorrectNode(current):
            left_child = self.Heap[self.get_left_child(current)]
            right_child = self.Heap[self.get_right_child(current)]

            if left_child < right_child:
                if self.Heap[current] > left_child:
                    self.swap(current, self.get_left_child(current))
                    current = self.get_left_child(current)

            else:
                if self.Heap[current] > right_child:
                    self.swap(current, self.get_right_child(current))
                    current = self.get_right_child(current)

        self.elements.remove(return_value)
        return return_value

    def get_left_child(self, pos):
        left_child_index = 2 * pos
        if left_child_index >= self.maxsize:
            return None
        return left_child_index

    def get_right_child(self, pos):
        right_child_index = 2 * pos + 1
        if right_child_index >= self.maxsize:
            return None
        return right_child_index

    def is_element_in_heap(self, element):
        return element in self.elements

    def __str__(self):
        return str(self.Heap[1:])
