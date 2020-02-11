from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import subprocess
from typing import Any

from whichcraft import which

import os


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class CalledProcessError(RuntimeError):
    pass


def cmd_output(output, *cmd, **kwargs):  # type: (bool, *str, **Any) -> str
    retcode = kwargs.pop('retcode', 0)
    kwargs.setdefault('stdout', subprocess.PIPE)
    kwargs.setdefault('stderr', subprocess.PIPE)
    proc = subprocess.Popen(cmd, **kwargs)
    stdout, stderr = proc.communicate()
    stdout = stdout.decode('UTF-8')
    stderr = stderr.decode('UTF-8')
    print(stdout) if output else 0
    if retcode is not None and proc.returncode != retcode:
        print(stderr)
        raise CalledProcessError(cmd, retcode, proc.returncode, stdout, stderr)
    return stdout


def run_gradle_task(output, *tasks):  # type: (bool, *str) -> int
    if which('gradle') is None:
        print(f"{bcolors.FAIL}Gradle could not be detected.{bcolors.ENDC}")
        return 1

    try:
        print("{}Running 'gradle {}' with native gradle.{}".format(bcolors.OKBLUE, ' '.join(tasks), bcolors.ENDC))
        cmd_output(output, 'gradle', *tasks)
        return 0
    except CalledProcessError:
        print(f"{bcolors.FAIL}The above error occurred running gradle task.{bcolors.ENDC}")
        return 1


def run_gradle_wrapper_task(output, *tasks):  # type: (bool, *str) -> int
    if which('gradlew', path='.') is None:
        print(
            f"{bcolors.FAIL}Could not locate gradle wrapper. Initialize with `gradle wrapper`, "
            f"or remove the -w (--wrapper) flag to use native gradle.{bcolors.ENDC}"
        )
        return 1

    try:
        print("{}Running 'gradle {}' with wrapper enabled.{}".format(bcolors.OKBLUE, ' '.join(tasks), bcolors.ENDC))
        cmd_output(output, '.{}gradlew'.format(os.path.sep), *tasks)
        return 0
    except CalledProcessError as e:
        print(f"{bcolors.FAIL}The above error occurred running gradle wrapper task.{bcolors.ENDC}")
        return 1
