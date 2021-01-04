# Introduction 

GaugeDepend is a dependency analysis tool for generating, visualizing and exploring dependency graphs for Gauge test suites. 
Such as visualization will allow quality assessment of test-automation scripts.

## What problem does GaugeDepend address? / Why should one use this tool?

As automated test suites grow, test scripts could start to become unorganized and suffer from various test "smells", e.g., test duplication. While the [Gauge](https://www.gauge.org) testing framework is a powerful BDD testing tool, our experience in developing and maintaining several large-scale Gauge test suites has shown that, especially when multiple test engineers are involved in developing large Gauge test suites, those test suites would often start to become unorganized, complex and messy; and internal quality of test code would start going down. 

As a software engineer, Karl Seguin, said in [a blog post](http://codebetter.com/karlseguin/2009/09/12/unit-testing-do-repeat-yourself/): *“Complex and mess[y] tests don’t add any value even if the code under test is perfectly designed”*.

Dependency analysis is a proven technique for visualizing, exploring and pinpointing issues in the way methods and classes in regular (production) code call each other. Visualizing of dependencies in regular (production) code-base has been around for many years, e.g., see tools such as [NDepend](https://www.ndepend.com) [pJDepend]( https://github.com/clarkware/jdepend), [SourceTrail](https://www.sourcetrail.com). We have taken the novel step of conducting dependency analysis in the test-code space, and have found that it is a promising technique for visualizing, exploring and pinpointing issues in the way that test scripts call each other.

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

## Development team and timeline
* [Connor Boyle](https://www.linkedin.com/in/connor-boyle-7239a0150/), Final Year CS student

* [Dr. Vahid Garousi](https://www.vgarousi.com), Associate Professor of Software Engineering, Queen’s University Belfast, Northern Ireland, UK

The project was completed during Spring 2020, as a student project in [Queen’s University Belfast](https://www.qub.ac.uk).

## Demo videos
A general overview of the tool's features and its code-base:

<a href="http://www.youtube.com/watch?feature=player_embedded&v=KTqZ4sITg4Y" target="_blank"><img src="http://img.youtube.com/vi/KTqZ4sITg4Y/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>

More videos, showing tool's features and benefits, will be published soon.
