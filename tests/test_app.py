import pytest
import sys
import os

from src.tornps import app

def test_dummy():
    t = app.dummy()
    assert t

