from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import subprocess
from typing import Any

from whichcraft import which

import os


class CalledProcessError(RuntimeError):
    pass


def cmd_output(*cmd, **kwargs):  # type: (*str, **Any) -> str
    retcode = kwargs.pop('retcode', 0)
    kwargs.setdefault('stdout', subprocess.PIPE)
    kwargs.setdefault('stderr', subprocess.PIPE)
    kwargs.setdefault('shell', True)
    proc = subprocess.Popen(cmd, **kwargs)
    stdout, stderr = proc.communicate()
    stdout = stdout.decode('UTF-8')
    print(stdout)
    if retcode is not None and proc.returncode != retcode:
        raise CalledProcessError(cmd, retcode, proc.returncode, stdout, stderr)
    return stdout


def run_gradle_task(*tasks):  # type: (*str) -> int
    if which('gradle') is None:
        print('Gradle could not be detected.')
        return 1

    try:
        print('Running gradle task with native gradle.')
        cmd_output('gradle', *tasks)
    except CalledProcessError as e:
        print('An error occurred running gradle task:\n')
        print(str(e))
        return 1

    return 0


def run_gradle_wrapper_task(*tasks):  # type: (*str) -> int
    if which('gradlew', path='.') is None:
        print(
            'Could not locate gradle wrapper. Initialize with `gradle wrapper`, or remove the -w (--wrapper) flag to '
            'use native gradle.'
        )
        return 1

    try:
        print('Running gradle task with wrapper enabled.')
        cmd_output('.{}gradlew'.format(os.path.sep), *tasks)
    except CalledProcessError as e:
        print('An error occurred running gradle wrapper task:\n')
        print(str(e))
        return 1

    return 0
