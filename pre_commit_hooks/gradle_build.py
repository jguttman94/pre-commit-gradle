from __future__ import print_function

import os
import argparse
from typing import Optional
from typing import Sequence

from pre_commit_hooks.util import cmd_output, run_gradle_wrapper_task, run_gradle_task


def main(argv=None):  # type: (Optional[Sequence[str]]) -> int
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-w', '--wrapper', action='store_true',
        help='Runs commands using gradlew. Requires gradle wrapper configuration within the project.'
    )
    parser.add_argument(
        '-o', '--output', action='store_true',
        help='Prints the output of all executed gradle commands.'
    )
    parser.add_argument(
        '-p', '--path', action='store_true', default = os.getcwd(),
        help='Path to gradle executable; if omitted, it is assumed gradle is installed at project root'
    )
    args = parser.parse_args(argv)

    if args.wrapper:
        return run_gradle_wrapper_task(args.output, args.path, 'build')
    else:
        return run_gradle_task(args.output, args.path, 'build')


if __name__ == '__main__':
    exit(main())
