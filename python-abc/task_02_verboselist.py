#!/usr/bin/env python3

class VerboseList(list):

    def append(self, my_item):
        super().append(my_item)
        print("Added [{}] to the list.".format(my_item))

    def extend(self, my_item):
        super().extend(my_item)
        print("Extended the list with [{}] items.".format(len(my_item)))

    def remove(self, my_item):
        print("Removed [{}] from the list.".format(my_item))
        super().remove(my_item)

    def pop(self, my_item=None):
        if (my_item is None):
            item = super().pop()
            print("Popped [{}] from the list.".format(item))
            return item
        else:
            item = super().pop(my_item)
            print("Popped [{}] from the list.".format(item))
