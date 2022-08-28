from __future__ import absolute_import
from __future__ import unicode_literals

import os
import pytest

from pre_commit_hooks.util import CalledProcessError
from pre_commit_hooks.util import cmd_output
from pre_commit_hooks.util import run_gradle_task
from pre_commit_hooks.util import run_gradle_wrapper_task


def test_raises_on_error():
    with pytest.raises(CalledProcessError):
        cmd_output('exit 1')


def test_output():
    ret = cmd_output('echo', 'hi', output=True)
    assert ret == 'hi\n'

def test_cwd():
    path = os.getcwd()
    testing = os.path.abspath(os.path.join(path, 'testing'))
    ret = cmd_output('ls', output=True, cwd=testing)
    assert ret == "__init__.py\nutil.py\n"


def test_run_gradle_task():
    path = os.getcwd()
    example = os.path.abspath(os.path.join(path, os.path.join('tests', 'example')))
    out = run_gradle_task(True, example,'build')
    assert out == 0

def test_run_gradle_task__ProcessingError():
    path = os.getcwd()
    example = os.path.abspath(os.path.join(path, os.path.join('tests', 'example')))
    out = run_gradle_task(True, example, 'exit 1')
    assert out == 1

def test_run_gradlew_task():
    path = os.getcwd()
    example = os.path.abspath(os.path.join(path, os.path.join('tests', 'example')))
    out = run_gradle_wrapper_task(True, example,'build')
    assert out == 0

def test_run_gradlew_task__ProcessingError():
    path = os.getcwd()
    example = os.path.abspath(os.path.join(path, os.path.join('tests', 'example')))
    out = run_gradle_wrapper_task(True, example, 'exit 1')
    assert out == 1

def test_run_gradlew_task__MissingExe():
    path = os.getcwd()
    example = os.path.abspath(os.path.join(path, os.path.join('tests')))
    out = run_gradle_wrapper_task(True, example, 'build')
    assert out == 1