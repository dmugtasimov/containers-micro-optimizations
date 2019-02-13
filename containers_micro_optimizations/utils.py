import sys
from io import StringIO
from collections import namedtuple

import pytablewriter
from terminaltables import AsciiTable
from pympler import asizeof


Measurement = namedtuple('Measurement', ('name', 'value'))


def get_title_lines(title):
    return title, '-' * len(title)


def print_title(title):
    print()
    print(title)
    print('=' * len(title))
    print()



def print_measurements(measurements, title=None):
    if title:
        print_title(title)
    headers = [('Collection type', 'Time, s', '% of best')]
    best = min(measurements, key=lambda x: x.value)
    rows = [
        (
            m.name,
            f'{m.value:.6g}' + (' *' if m.name == best.name else ''),
            f'{(m.value / best.value) * 100:.2f}',
         ) for m in measurements
    ]
    table = AsciiTable(headers + rows)
    table.justify_columns = {2: 'right'}
    print(table.table)
    print('* - best time')
    print()


def print_transposed_measurements(table_data, title=None):
    if title:
        print_title(title)

    headers = [list(table_data[0])]
    rows = []
    for row in table_data[1:]:
        new_row = [row[0]]
        best = min(row[1:])
        new_row.extend(f'{value:.6g}' + (' *' if value == best else '') for value in row[1:])
        rows.append(new_row)

    table = AsciiTable(headers + rows)
    print(table.table)
    print('* - best time')
    print()


class Spacemeter:

    HEADERS = ('Name', 'Size (sys.getsizeof), bytes', 'Size (pympler.asizeof), bytes')

    def __init__(self):
        self.measurements = []

    def measure(self, name, instance):
        self.measurements.append((name, sys.getsizeof(instance), asizeof.asizeof(instance)))

    def table(self):
        best = min(self.measurements, key=lambda x: x[2])[2]

        lines = []

        writer = pytablewriter.MarkdownTableWriter()
        writer.stream = StringIO()
        writer.headers = self.HEADERS
        writer.value_matrix = list(self.measurements)
        for index, value in enumerate(writer.value_matrix):
            if value[2] == best:
                writer.value_matrix[index] = (value[0] + ' *',) + value[1:]

        writer.write_table()

        lines.extend(writer.stream.getvalue().split('\n'))
        lines.append('\* - least space')
        return lines
