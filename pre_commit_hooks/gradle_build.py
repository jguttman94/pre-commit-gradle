from __future__ import print_function

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
    args = parser.parse_args(argv)

    tasks = ['build']
    return run_gradle_wrapper_task(*tasks) if args.wrapper else run_gradle_task(*tasks)


if __name__ == '__main__':
    exit(main())
