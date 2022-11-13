from one_hot_encoder import fit_transform
import pytest


def test_fit_transform_1():
    colors = ['red', 'red', 'green', 'blue', 'green']
    exp_transformed_colors = [
        ('red',   [0, 0, 1]),
        ('red',   [0, 0, 1]),
        ('green', [0, 1, 0]),
        ('blue',  [1, 0, 0]),
        ('green', [0, 1, 0]),
    ]
    transformed_colors = fit_transform(colors)
    assert transformed_colors == exp_transformed_colors


def test_fit_transform_2():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    exp_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    transformed_cities = fit_transform(cities)
    assert transformed_cities, exp_transformed_cities


def test_fit_transform_3():
    words = ['hello', 'word']
    exp_transformed_words = [
        ('hello', [0, 1]),
        ('word',  [1, 0]),
    ]
    transformed_words = fit_transform(words)
    assert transformed_words == exp_transformed_words


def test_fit_transform_4():
    letters = list('abcde')
    exp_transformed_letters = [
        ('a', [0, 0, 0, 0, 1]),
        ('b', [0, 0, 0, 1, 0]),
        ('c', [0, 0, 1, 0, 0]),
        ('d', [0, 1, 0, 0, 0]),
        ('e', [1, 0, 0, 0, 0]),
    ]
    transformed_letters = fit_transform(letters)
    assert transformed_letters == exp_transformed_letters


def test_fit_transform_exception_1():
    """Test 1 that an exception is raised"""
    with pytest.raises(TypeError) as err:
        fit_transform()

    assert err.value.args[0] == 'expected at least 1 arguments, got 0'


def test_fit_transform_exception_2():
    """Test 2 that an exception is raised"""
    with pytest.raises(TypeError) as err:
        fit_transform(1)

    assert err.value.args[0] == "'int' object is not iterable"
