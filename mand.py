import os
import re
import sys
import textwrap

try:
    from termcolor import colored
except:
    colored = lambda arg, *args, **kwargs: arg

EXIT_FAILURE = 1
EXIT_CODE_NO_FILE = 2
SHELLMANDS_FILENAME = os.path.join(os.getcwd(), '.shellmands')
SUB_PATTERN = re.compile(r'^\s*([a-zA-Z0-9_-]+)\s*\(\)\s*\{')

def usage():
    print('Usage: mand {list|map}', file=sys.stderr)
    sys.exit(EXIT_FAILURE)

def get_action():
    if len(sys.argv) < 2:
        usage()
    elif sys.argv[1] not in ['list', 'map']:
        usage()

    return sys.argv[1]

def assert_file_exists(filename):
    if not os.path.isfile(filename):
        print(f'File {filename} is missing', file=sys.stderr)
        sys.exit(EXIT_CODE_NO_FILE)

def read_shellmands(filename):
    print(filename)
    with open(filename) as f:
        lines = [line.rstrip('\n') for line in f]

    accumulator = []
    shellmands = []

    for line in lines:
        m = SUB_PATTERN.match(line)

        if m:
            prev_comment = [i[1:] for i in accumulator[::-1] if i.startswith('#')][::-1]
            prev_comment = '\n'.join(prev_comment)
            description = textwrap.dedent(prev_comment).replace('\n', ' ')

            shellmands.append((m.group(1), description))
            accumulator = []
        else:
            accumulator.append(line)

    return shellmands

if __name__ == "__main__":
    action = get_action()

    assert_file_exists(SHELLMANDS_FILENAME)

    if action == 'list':
        shellmands = read_shellmands(SHELLMANDS_FILENAME)

        print('Here are the ' + colored('shellmands', 'green') + ' in this directory:')
        for funcname, description in shellmands:
            print()
            print('    ' + colored(funcname, 'blue'))
            print('\n'.join('        ' + i for i in textwrap.wrap(description, 60)))
