Development of a tool to visualize the dependencies among test suites and the web services called by them
------------------------------------------------------------------------------------------------------

GaugeDependExtended is a dependency analysis tool for generating, visualizing and exploring dependency graphs for Gauge test suites and the web services called by them. 
Such visualization will allow quality assessment of test-automation scripts being developed for web applications.

## What problem does GaugeDependExtended address? / Why should one use this tool?

Software testing is an industry standard for web developers and software engineers. When developing a web application, engineers have found that the test code often has errors and inefficiencies. To help prevent this, continual quality assessment and maintenance is necessary to ensure that the tests are repeatable, predictable, and efficiently executed.  

The visualisation of client-side and server-side test dependencies will allow software test engineers to conduct dependency analysis and assist with quality assessment and maintenance of the test suites.

![alt text](https://gitlab2.eeecs.qub.ac.uk/40206673/vg03-csc3002-40206673/blob/master/resources/petclinic_graph.PNG?raw=true)

## Getting Started 
To install this project simply clone the repo and run the following commands to install the dependencies and application modules (Tested using Python version 3.8.8).
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
We have developed a unit test suite for the GaugeDependExtended project, using the Python unit testing framework. The unit tests for this project are contained in the `test` directory, they can either be executed individually or all unit test can be executed by running the following command in the root directory of this project. 
```
python -m unittest discover -v
```

## Development team and timeline
* [Cameron Brush](https://www.linkedin.com/in/cameronbrush/), Final Year CS student

* [Dr. Vahid Garousi](https://www.vgarousi.com), Associate Professor of Software Engineering, Queen’s University Belfast, Northern Ireland, UK

The project was completed during Autumn 2020 - spring 2021, as a student project in [Queen’s University Belfast](https://www.qub.ac.uk).

This project is an extension of [GaugeDepend](https://github.com/vgarousi/GaugeDepend) .
---------------------------------------------------------------------------------------------------------