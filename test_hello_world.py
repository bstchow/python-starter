import io
import sys
import pytest

from hello_world import hello_world

def test_print():
    assert hello_world() == "Hello World";
