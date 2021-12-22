import pytest
from pizza import *
from unittest.mock import patch


@pytest.mark.parametrize('actual, expected', [
    (Margherita('XL'), Margherita('XL')),
    (Hawaiian(), Hawaiian('L')),
    (Pepperoni('L'), Pepperoni())
])
def test_eq(actual, expected):
    assert actual == expected


@pytest.mark.parametrize('actual, expected', [
    (Margherita('XL'), 'pizza'),
    (Hawaiian('XL'), Hawaiian('L')),
    (Pepperoni('L'), Hawaiian('L'))
])
def test_not_eq(actual, expected):
    assert actual != expected


def test_dict():
    actual = Pepperoni().dict()
    expected = ['tomato sauce', 'mozzarella', 'pepperoni']
    assert actual == expected


def test_unacceptable_size():
    with pytest.raises(ValueError):
        Hawaiian('M')


def test_bake():
    expected = '✔ Приготовили за 15 мин!'
    with patch.object(random, 'randint', return_value=15):
        actual = bake(Hawaiian('L'))
    assert actual == expected


def test_deliver():
    expected = '🛵 Доставили за 12 мин!'
    with patch.object(random, 'randint', return_value=12):
        actual = deliver(Hawaiian('L'))
    assert actual == expected


def test_pick_up():
    expected = '🏠 Забрали за 16 мин!'
    with patch.object(random, 'randint', return_value=16):
        actual = pick_up(Hawaiian('L'))
    assert actual == expected

