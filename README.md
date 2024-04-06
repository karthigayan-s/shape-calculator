# shape-calculator
Repository to maintain shape calculator application

## Setup:

If your machine running python3.x (3.11 preferred) then you can directly access the application. If not create virtual environment and run. Follow the below steps.

$ source env/bin/activate

$ pip install -r requirements.txt 

## Usage Example:

$ ./calculate.py CIRCLE AREA 20

$ ./calculate.py RECTANGLE AREA 10 20

$ ./calculate.py SPHERE VOLUME 30

$ ./calculate.py CUBOID VOLUME 10 10 20

## Test:

From base folder run all tests using following command,

$ pytest test/test_shape_calculator.py

Example to run any single test

$ pytest test/test_shape_calculator.py::test_calculate_area_of_rectangle
