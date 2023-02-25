# TEST VAGRANT CODING ASSIGNMENT


## TOOLS
* Python - 3.10
* allure-pytest - 2.11.1
* allure-python-commons - 2.11.1
* openpyxl - 3.0.10
* pandas - 1.5.0
* pendulum - 2.1.2
* pytest - 7.1.3
* selenium - 4.5.0
* webdriver-manager - 3.8.3
* pytest-html

## GIT LINK TO CLONE PROJECT

> git clone 

## HOW TO EXECUTE IN COMMAND LINE
> pytest -m marker_name
> pytest module.py::ClassName::method_name

## To change grouping of scripts (change marker_name)
> Markers are used for grouping tests

## For reports option
> --html=report.html 

## For rerunning failed tests
> pipenv run pytest --lf

## For parallel execution 
> -n number_of_workers (input_type = integer)

## HOW TO RUN SCRIPT IN DIFFERENT BROWSER
> pytest module.py::ClassName::method_name --browser=edge
