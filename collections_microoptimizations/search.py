from itertools import chain
from timeit import timeit, default_number

from collections_microoptimizations.utils import (
    Measurement, print_measurements, print_transposed_measurements)


def make_collection(collection_type, size, value_type):
    supported_collection_types = (tuple, list, dict, set, frozenset)
    if not issubclass(collection_type, supported_collection_types):
        raise ValueError(f'"collection_type" must be one of: {supported_collection_types!r}')

    supported_value_types = (int, str)
    if not issubclass(value_type, supported_value_types):
        raise ValueError(f'"value_type" must be one of: {supported_value_types!r}')

    if issubclass(collection_type, dict):
        return collection_type((value_type(x), value_type(x)) for x in range(size))
    else:
        return collection_type(map(value_type, range(size)))


def get_collection_timeit(collection_type, collection_size, value):
    statement = f'{value!r} in collection'
    collection = make_collection(collection_type, collection_size, type(value))
    return timeit(statement, globals={'collection': collection})


def get_collection_timeit_for_value_size(collection_type, collection_size, value_size):
    return get_collection_timeit(collection_type, collection_size, value='a' * value_size)


def get_collection_size_vs_collection():
    headers = ('Size', 'tuple, O(n)', 'list, O(n)', 'dict, O(1)*', 'set, O(1)*',
               'frozenset, O(1)*')
    rows = []

    for size in chain(range(11), (100,)):
        row = [str(size)]
        row.append(get_collection_timeit(tuple, size, -1))
        row.append(get_collection_timeit(list, size, -1))
        row.append(get_collection_timeit(dict, size, -1))
        row.append(get_collection_timeit(set, size, -1))
        row.append(get_collection_timeit(frozenset, size, -1))
        rows.append(row)

    return [headers] + rows


def get_value_size_vs_collection(collection_size):
    headers = ('Size', 'tuple, O(n)', 'list, O(n)', 'dict, O(1)*', 'set, O(1)*',
               'frozenset, O(1)*')
    rows = []

    for size in chain(range(11), (100, 1000, 10000)):
        row = [str(size)]
        row.append(get_collection_timeit_for_value_size(tuple, collection_size, size))
        row.append(get_collection_timeit_for_value_size(list, collection_size, size))
        row.append(get_collection_timeit_for_value_size(dict, collection_size, size))
        row.append(get_collection_timeit_for_value_size(set, collection_size, size))
        row.append(get_collection_timeit_for_value_size(frozenset, collection_size, size))
        rows.append(row)

    return [headers] + rows


# print_transposed_measurements(
#     get_collection_size_vs_collection(),
#     title=f'Search of an integer in a varying size collection ({default_number} times)')
# print_transposed_measurements(
#     get_value_size_vs_collection(0),
#     title=f'Search of a varying size string in an empty collection ({default_number} times)')
for value_size in range(10):
    print_transposed_measurements(
        get_value_size_vs_collection(value_size),
        title=f'Search of a varying size string in a collection of {value_size} elements '
              f'({default_number} times)')
