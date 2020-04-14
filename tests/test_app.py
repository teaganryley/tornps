import pytest
import sys,os

# ensures pytest will locate project without having to run setup.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import src.tornps.app as app

def test_dummy():
    t = app.dummy()
    assert t

