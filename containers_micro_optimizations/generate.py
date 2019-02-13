import argparse
import os
import os.path
import subprocess

from jinja2 import Environment, PackageLoader, select_autoescape

BUILD_DIR = './build'
INDEX_FILE = BUILD_DIR + '/index.md'


def run(command, with_command=False):
    lines = []
    if with_command:
        lines.append(f'$ {command}')

    output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True,
                                     encoding='utf-8')
    lines.append(output)
    return '\n'.join(lines)


def entry():

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     prog='containers-micro-optimizations-generate')
    parser.add_argument('-b', '--build-dir', help='Build directory', default='./_build')
    parser.add_argument('-i', '--index-file', help='Index file name', default='index.md')
    args = parser.parse_args()

    env = Environment(
        loader=PackageLoader('containers_micro_optimizations', 'templates'),
        autoescape=select_autoescape(('html', 'xml')))
    template = env.get_template('index.j2.md')

    build_dir = args.build_dir
    os.makedirs(build_dir, exist_ok=True)

    index_file = args.index_file
    index_file_full_path = os.path.join(build_dir, index_file)
    with open(index_file_full_path, 'w') as f:
        f.write(template.render(run=run))
