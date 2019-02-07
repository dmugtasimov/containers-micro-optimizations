from collections import namedtuple

from terminaltables import AsciiTable


Measurement = namedtuple('Measurement', ('name', 'value'))


def print_measurements(measurements, title=None):
    if title:
        print()
        print(title)
        print('=' * len(title))
        print()
    headers = [('Collection type', 'Time, s', '% of best')]
    best = min(measurements, key=lambda x: x.value)
    data = [
        (
            m.name + (' *' if m.name == best.name else ''),
            f'{m.value:.6g}',
            f'{(m.value / best.value) * 100:.2f}',
         ) for m in measurements
    ]
    table = AsciiTable(headers + data)
    table.justify_columns = {2: 'right'}
    print(table.table)
    print('* - best time')
    print()
