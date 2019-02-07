from timeit import timeit, default_number

from collections_microoptimizations.utils import Measurement, print_measurements


def get_empty_measurements():
    return (
        Measurement('tuple', timeit('()')),
        Measurement('list', timeit('[]')),
        Measurement('dict', timeit('{}')),
        Measurement('frozenset', timeit('frozenset()')),
        Measurement('set', timeit('set()')),
    )


def get_one_element_measurements():
    int_increment_time = timeit('x += 1', setup='x = 0')
    int_element_increment_time = timeit('x[0] += 1', setup='x = [0]')
    return (
        Measurement('tuple', timeit('x += 1; (x,)', setup='x = 0') - int_increment_time),
        Measurement('list', timeit('x += 1; [x]', setup='x = 0') - int_increment_time),
        Measurement('dict', timeit('x += 1; {x: x}', setup='x = 0') - int_increment_time),
        Measurement('frozenset', timeit('x[0] += 1; frozenset(x)', setup='x = [0]') - int_element_increment_time),
        Measurement('set', timeit('x[0] += 1; set(x)', setup='x = [0]') - int_element_increment_time),
    )


print_measurements(get_empty_measurements(),
                   title=f'Instantiation of an empty collection ({default_number} times)')
print_measurements(get_one_element_measurements(),
                   title=f'Instantiation of a collection with one element ({default_number} times)')
