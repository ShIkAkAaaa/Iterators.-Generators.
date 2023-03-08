class FlatIterator:

    def __init__(self, list_of_list_1):
        self.list_of_list_1 = list_of_list_1

    def __iter__(self):
        self.number = 0
        self.number1 = -1

        return self

    def __next__(self):
        if self.number1 == len(self.list_of_list_1[self.number])-1:
            self.number += 1
            self.number1 = -1

        if self.number == len(self.list_of_list_1):
            raise StopIteration

        self.number1 += 1

        return self.list_of_list_1[self.number][self.number1]


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()

import types


def flat_generator(list_of_lists):

    list_1 = []
    a = 0
    for item in list_of_lists:
        for items in item:
            list_1.append(items)
    while a < len(list_1):
        yield list_1[a]
        a += 1



def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()