#########################################
# Filename: shape_calculator.py
# Description: Module to maintain share calculator related classes and constants
##########################################
import sys
from math import pi

SUPPORTED_OPERATIONS = ['AREA', 'VOLUME']

SUPPORTED_SHAPES_AND_OPERATION_MAP = {'CIRCLE': ['AREA'],
                            'RECTANGLE': ['AREA'],
                            'SPHERE': ['VOLUME'],
                            'CUBOID': ['VOLUME']
                            }


class InputParamException(Exception):
    pass

class ShapeCalculator:
    def __init__(self, shape, operation, values):
        """
        Constructor for the ShapeCalculator.
        It sets all value to the object for do further operation
        :param shape: Shape to do operation
        :param operation: Operation
        :param values: Input value for the calculation
        """
        self.shape=shape
        self.operation=operation
        self.values=values

    def calculate(self):
        """
        Method to calculation based on the inputs
        :return: Result of the calculation
        """
        if self.shape == 'CIRCLE' and self.operation == 'AREA':
            return self.calculate_area_of_circle()
        elif self.shape == 'RECTANGLE' and self.operation == 'AREA':
            return self.calculate_area_of_rectangle()
        elif self.shape == 'SPHERE' and self.operation == 'VOLUME':
            return self.calculate_volume_of_sphere()
        elif self.shape == 'CUBOID' and self.operation == 'VOLUME':
            return self.calculate_volume_of_cuboid()

    def calculate_area_of_circle(self):
        """
        Method to calculate area of circle
        :return: Rounded area of circle
        """
        if len(self.values) != 1:
            raise InputParamException("Please provide radius value")
        return round(pi * self.values[0] * self.values[0])

    def calculate_area_of_rectangle(self):
        """
        Method to calculate area of recrangle
        :return: Rounded area of rectangle
        """
        if len(self.values) != 2:
            raise InputParamException("Please provide length and width")
        return round(self.values[0] * self.values[1])

    def calculate_volume_of_sphere(self):
        """
        Method to calculate volume of sphere
        :return: Rounded volume of sphere
        """
        if len(self.values) != 1:
            raise InputParamException("Please provide radius value")
        return round(4.0/3.0 * pi * self.values[0]**3)

    def calculate_volume_of_cuboid(self):
        """
        Method to calculate volume of cuboid
        :return: Rounded volume of cuboid
        """
        if len(self.values) != 3:
            raise InputParamException("Please provide length, breadth and height values")
        return round(self.values[0] * self.values[1] * self.values[2])