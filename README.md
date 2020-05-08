# Introduction 

GaugeDepend project is a dependency analysis tool for generating, visualizing and exploring dependency graphs for Guage test suites. 
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
We have developed a unit test suite for the GaugeDepend project, using the Python unit testing framework. The unit tests for this project are contained in the `test` directory, they can either be executed individually or all unit test can be executed by running the following command in the root directory of this project. 
```
python -m unittest discover -v
```
A Gitlab CI runner has been set up for this project and the unit tests are run automatically on commit.

## Development team and timeline
* [Connor Boyle](https://www.linkedin.com/in/connor-boyle-7239a0150/), Final Year CS student

* [Dr. Vahid Garousi](https://www.vgarousi.com), Associate Professor of Software Engineering, Queen’s University Belfast, Northern Ireland, UK

The project was completed during Spring 2020, as a student project in [Queen’s University Belfast](https://www.qub.ac.uk).

## Demo videos
A general review of the code-base and tool's feature, narrated by Connor Boyle:

<a href="http://www.youtube.com/watch?feature=player_embedded&v=KTqZ4sITg4Y" target="_blank"><img src="http://img.youtube.com/vi/KTqZ4sITg4Y/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>

---
Application of the tool on the Gauge test suites of a large web application, named [Testinium](https://www.testinium.com), narrated by Vahid Garousi:
```
Will be published soon.
```
