from itertools import chain
from timeit import timeit, default_number

from collections_microoptimizations.utils import (
    Measurement, print_measurements, print_transposed_measurements)


def get_search_in_empty_collection_measurements(value):
    statement = f'{value!r} in c'
    return (
        Measurement('tuple,      O(n)', timeit(statement, setup='c = ()')),
        Measurement('list,       O(n)', timeit(statement, setup='c = []')),
        Measurement('dict,       O(1)*', timeit(statement, setup='c = {}')),
        Measurement('set,        O(1)*', timeit(statement, setup='c = set()')),
        Measurement('frozenset,  O(1)*', timeit(statement, setup='c = frozenset()')),
    )


def get_search_in_non_empty_collection_measurements(value, fill_in_func=range):
    statement = f'{value!r} in c'

    headers = ('Size', 'tuple, O(n)', 'list, O(n)', 'dict, O(1)*', 'set, O(1)*',
               'frozenset, O(1)*')
    rows = []

    for size in chain(range(11)):
        row = [str(size)]
        row.append(timeit(statement, setup='c = ({})'.format(''.join(map(lambda x: f'{x!r},', fill_in_func(size))))))
        row.append(timeit(statement, setup='c = [{}]'.format(','.join(map(repr, fill_in_func(size))))))
        row.append(timeit(statement, setup='c = {{}}'.format(','.join(f'{x!r}:{x!r}' for x in fill_in_func(size)))))
        row.append(timeit(statement, setup='c = set([{}])'.format(','.join(map(repr, fill_in_func(size))))))
        row.append(timeit(statement, setup='c = frozenset([{}])'.format(','.join(map(repr, fill_in_func(size))))))
        rows.append(row)

    return [headers] + rows


print_measurements(get_search_in_empty_collection_measurements(1),
                   title=f'Search of an integer in an empty collection ({default_number} times)')
print_measurements(get_search_in_empty_collection_measurements('a'),
                   title=f'Search of a one character string in an empty collection '
                         f'({default_number} times)')
print_transposed_measurements(get_search_in_non_empty_collection_measurements(1),
                              title=f'Search of an integer in a collection ({default_number} times)')
print_transposed_measurements(get_search_in_non_empty_collection_measurements('a'),
                              title=f'Search of a one character string in a collection ({default_number} times)')
