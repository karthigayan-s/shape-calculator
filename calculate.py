#!/usr/bin/env python3
###################################
# Filename: calculate.py
# Description: Application to calculate area of Circle and Rectangle and Volume of Sphere and Cuboid
###################################

import sys

from lib.shape_calculator import ShapeCalculator, SUPPORTED_OPERATIONS, SUPPORTED_SHAPES_AND_OPERATION_MAP

def parse_and_validate_args():
    """
    Function to parse the command line arguments and validate them
    :return: Shape, operation and input values
    """
    args = sys.argv[1:]
    values = list()
    error = False

    if len(args) < 3:
        help()

    if args[0] not in SUPPORTED_SHAPES_AND_OPERATION_MAP.keys():
        error = True
        print(f"Unknown shape: {args[0]}")

    if args[1] not in SUPPORTED_OPERATIONS:
        error = True
        print(f"Unsupported operation: {args[1]}")
    elif args[1] not in SUPPORTED_SHAPES_AND_OPERATION_MAP[args[0]]:
        error = True
        print(f"Unsupported operation {args[1]} for shape {args[0]}")

    if error:
        sys.exit(1)

    # Converting string to text to do math operation
    for value in args[2:]:
       values.append(int(value))

    return args[0], args[1], values


def help():
    """
    Function to print help message for the user
    :return: None
    """
    help = '''Not enough arguments, Please find the samples
    calculate.py CIRCLE AREA <RADIUS>
    calculate.py RECTANGLE AREA <LENGTH> <WIDTH>
    calculate.py SPHERE VOLUME <RADIUS>
    calculate.py CUBOID VOLUME <LENGTH> <BREATH> <HEIGHT>
    '''
    sys.exit(help)

if __name__ == '__main__':
    (shape, operation, values) = parse_and_validate_args()
    shape_calc=ShapeCalculator(shape, operation, values)
    result=shape_calc.calculate()
    print(f"result = [{result}]")
