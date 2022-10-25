from pandas.core.common import flatten


NESTED_LIST = [
	['a', 'b', 'c', [1, 2, 3, [3, 4]]],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]


class FlatIterator:

    def __init__(self, nested_list):
        self.nested_list = nested_list

    def __iter__(self):
        self.flatted_list = list(flatten(self.nested_list))
        return iter(self.flatted_list)

    def __next__(self):
        k = 0
        while k > len(self.flatted_list):
            self.step = self.flatted_list[k - 1]
            k += 1
            if k >= len(self.flatted_list):
                raise StopIteration
            yield self.flatted_list[k - 1]


def flat_generator(lis):
    flatted = list(flatten(lis))
    k = 0
    while k < len(flatted):
        yield flatted[k]
        k += 1


if __name__ == '__main__':
    print('Generator:')
    for i in flat_generator(NESTED_LIST):
        print(i)
    print('\nIterator:')
    test = FlatIterator(NESTED_LIST)
    for i in test:
        print(i)
    print('\nIterator with list comprehension:')
    flat = [i for i in test]
    print(flat)