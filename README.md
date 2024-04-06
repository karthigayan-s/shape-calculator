# shape-calculator
Repository to maintain shape calculator application

Setup:
If your machine running python3.x then you can directly access the application. If not create virtual environment and run. Follow the below steps.

$ source env/bin/activate
$ pip install -r requirements.txt 

Usage:
$ ./calculate.py CIRCLE AREA <RADIUS>
$ ./calculate.py RECTANGLE AREA <LENGTH> <WIDTH>
$ ./calculate.py SPHERE VOLUME <RADIUS>
$ ./calculate.py CUBOID VOLUME <LENGTH> <BREATH> <HEIGHT>

Test:
From base folder run all tests using following command,
$ pytest test/test_shape_calculator.py

Example to run any single test
$ pytest test/test_shape_calculator.py::test_calculate_area_of_rectangle
