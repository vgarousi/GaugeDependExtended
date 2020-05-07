# GaugeDepend

This project is a dependency analysis tool for generating, visualizing and exploring dependency graphs for Guage test suites. 
Such as visualization will allow quality assessment of test-automation scripts.

## Getting Started 
To install this project simply clone the repo and run the following commands to install the dependencies and application modules.
```
pip install -r requirements.txt
```
```
pip install .
```

Then to launch the application execute the file `main.py` e.g. 
```
python application/main.py
```

## Running the tests
The unit tests for this project are contained in the `test` directory, they can either be executed individually or all unit test can be executed by running the following command in the root directory of this project. 
```
python -m unittest discover -v
```
A Gitlab CI runner has been set up for this project and the unit tests are run automatically on commit.

## Development team 
Connor Boyle: https://www.linkedin.com/in/connor-boyle-7239a0150/

Dr. Vahid Garousi: https://www.vgarousi.com
Associate Professor of Software Engineering
Queen’s University Belfast, Northern Ireland, UK

The technical idea behind the tool was developed and provided by Dr. Vahid Garousi, and implementations were done by Connor Boyle. The project was conductred during Winter 2020.
