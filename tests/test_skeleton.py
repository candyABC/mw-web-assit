#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from src.mw_web_assit.skeleton import fib

__author__ = "candyabc"
__copyright__ = "candyabc"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
