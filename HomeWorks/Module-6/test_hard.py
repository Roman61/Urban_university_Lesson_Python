import pytest
import math
from hard import Figure, Triangle, Cube


def test_set_sides():
    figure = Figure(None, 10, 20, 30)
    assert figure.get_sides() == [10, 20, 30]

    figure = Figure(None, 50)
    assert figure.get_sides() == [50, 50, 50]

    with pytest.raises(AssertionError):
        figure = Figure(None, 10, 20)


def test_set_color():
    figure = Figure(None, 10, 20, 30)
    figure.set_color(255, 128, 0)
    assert figure.get_color() == [255, 128, 0]

    with pytest.raises(AssertionError):
        figure.set_color(300, 128, 0)


def test_len():
    figure = Figure(None, 10, 20, 30)
    assert len(figure) == 60

    figure = Figure(None, 50)
    assert len(figure) == 150


def test_circle_radius():
    circle = Circle(None, 62.8)
    assert round(circle.radius, 2) == 10.0


def test_circle_square():
    circle = Circle(None, 62.8)
    assert round(circle.get_square(), 2) == 314.16


def test_triangle_square():
    triangle = Triangle(None, 3, 4, 5)
    assert triangle.get_square() == 6

    triangle = Triangle(None, 6, 8, 10)
    assert triangle.get_square() == 24


def test_triangle_sides():
    triangle = Triangle(None, 3, 4, 5)
    assert triangle.sides == [3, 4, 5]

    with pytest.raises(AssertionError):
        triangle = Triangle(None, 3, 4)


def test_cube_volume():
    cube = Cube(None, 5)
    assert cube.get_volume() == 125

    cube = Cube(None, 10)
    assert cube.get_volume() == 1000


def test_cube_sides():
    cube = Cube(None, 5)
    assert cube.sides == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]

    with pytest.raises(AssertionError):
        cube = Cube(None, 5, 5)
