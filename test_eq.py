from scr.card import Card

def test_eq():
    assert Card('blue', 5) == Card('blue', 5)
    assert Card('red', 3) == Card('green', 3)
    assert Card('blue', 5) != Card('blue', 6)