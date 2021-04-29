#!/usr/bin/env python

"""Tests for the simit.my_module module.
"""
import sys
import pytest
from simit import my_module
from testfixtures import LogCapture


def test_log_capture(caplog):
    with LogCapture() as lc:
        my_module.example()

    lc.check(
        ('simit.my_module', 'INFO', 'Providing information about the excecution of the function.')
    )


def test_module_import():
    assert my_module not in sys.modules


def test_something():
    assert True


def test_with_error():
    with pytest.raises(ValueError):
        # Do something that raises a ValueError
        raise(ValueError)


# Fixture example
@pytest.fixture
def an_object():
    return {}


def test_my_module(an_object):
    assert an_object == {}
