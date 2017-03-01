from sticks import switch_player

def test_switch_player():
    assert switch_player(False) == True
    assert switch_player(True) == False
