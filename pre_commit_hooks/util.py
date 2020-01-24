from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import subprocess
from typing import Any

import os


class InitializationError(RuntimeError):
    pass


class CalledProcessError(RuntimeError):
    pass


def cmd_output(*cmd, **kwargs):  # type: (*str, **Any) -> str
    retcode = kwargs.pop('retcode', 0)
    kwargs.setdefault('stdout', subprocess.PIPE)
    kwargs.setdefault('stderr', subprocess.PIPE)
    proc = subprocess.Popen(cmd, **kwargs)
    stdout, stderr = proc.communicate()
    stdout = stdout.decode('UTF-8')
    if retcode is not None and proc.returncode != retcode:
        raise CalledProcessError(cmd, retcode, proc.returncode, stdout, stderr)
    return stdout


def configure_gradle_wrapper() -> str:
    if not os.path.exists('.{}gradlew'.format(os.path.sep)):
        raise InitializationError('Could not locate gradle wrapper. Initialize with `gradle wrapper`, or remove the '
                                  '-w (--wrapper) flag to use native gradle.')

    return '.{}gradlew'.format(os.path.sep)
