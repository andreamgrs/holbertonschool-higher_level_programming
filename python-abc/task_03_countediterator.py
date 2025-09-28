#!/usr/bin/env python3

class CountedIterator:

    def __init__(self, my_data):
        self.cont = 0
        self.iter_obj = iter(my_data)

    def get_count(self):
        return self.cont

    def __iter__(self):
        return self

    def __next__(self):
        try:
            num = next(self.iter_obj)
            self.cont = self.cont + 1
            return num
        except StopIteration:
            raise StopIteration
