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

> git clone https://github.com/Shashi742744/test-vagrant

## HOW TO EXECUTE IN COMMAND LINE
> pytest -m marker_name
> 
> pytest module.py::ClassName::method_name

## TO CHANGE GROUPING OF SCRIPTS (CHANGE MAKER_NAME)
> Markers are used for grouping tests

## FOR REPORTS OPTION
> --html=report.html 

## FOR RERUNNING FAILED TESTS
> pipenv run pytest --lf

## HOW TO RUN SCRIPT IN DIFFERENT BROWSER
> pytest module.py::ClassName::method_name --browser=<browser_name>
