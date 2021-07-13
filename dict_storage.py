

class DictStorage:
    def __init__(self):
        self.elements = dict()

    def add(self, key, value):
        if key in self.elements:
            self.elements[key].append(value)
        else:
            self.elements[key] = [value]

    def remove(self, key):
        del self.elements[key]

    def contains(self, key):
        return key in self.elements

    def print_values(self):
        occurrences = 0
        for e in self.elements:
            for uuid in self.elements[e]:
                print(uuid, e)
                occurrences += 1

        return occurrences
