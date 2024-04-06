##################################
# Filename: test_shape_calculator.py
# Pytest module for shape_calculator
##################################
import pytest
import sys

sys.path.append('.')
from lib.shape_calculator import ShapeCalculator, InputParamException

def test_calculate_area_of_circle():
    """
    Test to validate area of circle functionality
    :return: None
    """
    calc=ShapeCalculator('CIRCLE', 'AREA', [5])
    assert calc.calculate() == 79

def test_calculate_area_of_rectangle():
    """
    Test to validate area of rectangle functionality
    :return: None
    """
    calc = ShapeCalculator('RECTANGLE', 'AREA', [10, 5])
    assert calc.calculate() == 50

def test_calculate_volume_of_sphere():
    """
    Test to validate volume of sphere functionality
    :return: None
    """
    calc = ShapeCalculator('SPHERE', 'VOLUME', [10])
    assert calc.calculate() == 4189

def test_calculate_volume_of_cuboid():
    """
    Test to validate volume of cuboid functionality
    :return: None
    """
    calc = ShapeCalculator('CUBOID', 'VOLUME', [10, 10, 10])
    assert calc.calculate() == 1000

def test_invalid_no_params_calculate_area_of_circle():
    """
    Negative test for area of circle
    :return: None
    """
    with pytest.raises(InputParamException):
        calc=ShapeCalculator('CIRCLE', 'AREA', [5, 10])
        calc.calculate()

def test_invalid_no_params_calculate_area_of_rectangle():
    """
    Negative test for area of rectangle
    :return: None
    """
    with pytest.raises(InputParamException):
        calc=ShapeCalculator('RECTANGLE', 'AREA', [5])
        calc.calculate()

def test_invalid_no_params_volume_of_sphere():
    """
    Negative test for volume of sphere
    :return: None
    """
    with pytest.raises(InputParamException):
        calc=ShapeCalculator('SPHERE', 'VOLUME', [10,20,30])
        calc.calculate()

def test_invalid_no_params_volume_of_cuboid():
    """
    Negative test for volume of cuboid
    :return: None
    """
    with pytest.raises(InputParamException):
        calc=ShapeCalculator('CUBOID', 'VOLUME', [10,20])
        calc.calculate()