from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import subprocess
from typing import Any

from whichcraft import which

import os


class InitializationError(RuntimeError):
    pass


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


def configure_gradle() -> str:
    if which('gradle') is None:
        raise InitializationError('Gradle could not be detected.')

    print('Running gradle-check with native gradle.')
    return 'gradle'


def configure_gradle_wrapper() -> str:
    if which('gradlew', path='.') is None:
        raise InitializationError('Could not locate gradle wrapper. Initialize with `gradle wrapper`, or remove the '
                                  '-w (--wrapper) flag to use native gradle.')

    print('Running gradle-check with wrapper enabled.')
    return '.{}gradlew'.format(os.path.sep)
