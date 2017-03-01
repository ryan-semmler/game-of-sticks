from AIsticks import switch_player
from AIsticks import create_entry
from AIsticks import add_to_entry
from AIsticks import sub_from_entry


def test_switch_player():
    assert switch_player(False) == True
    assert switch_player(True) == False


def test_create_entry():
    assert create_entry(4, {}) == {4: [1, 2, 3]}
    assert create_entry(2, {}) == {2: [1, 2]}
    assert create_entry(1, {}) == {1: [1]}
