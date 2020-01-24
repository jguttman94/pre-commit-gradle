from __future__ import print_function

import argparse
import os
from typing import Optional
from typing import Sequence

from pre_commit_hooks.util import cmd_output, configure_gradle_wrapper


def main(argv=None):  # type: (Optional[Sequence[str]]) -> int
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-w', '--wrapper', action='store_true',
        help='Runs commands using gradlew. Requires gradle wrapper configuration within the project.'
    )
    args = parser.parse_args(argv)

    cmd = 'gradle'
    if args.wrapper:
        cmd = configure_gradle_wrapper()

    cmd_output(cmd, 'check')

    return 0


if __name__ == '__main__':
    exit(main())
