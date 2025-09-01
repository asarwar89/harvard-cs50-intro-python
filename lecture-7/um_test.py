from um import count
import pytest

def test_count():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("UM") == 1
    assert count("Hello, um.") == 1
    assert count("Hello, um. How are you, um?") == 2
    assert count("Hello, world.") == 0
    assert count("Hello, uum.") == 0