GaugeDependExtended: A tool for automated visualisation of BDD test suites and their web-service dependencies
------------------------------------------------------------------------------------------------------

GaugeDependExtended is a dependency-analysis (visualisation) tool for generating, visualizing and exploring dependency graphs for test suites, developing using the BDD tool, [Gauge](https://gauge.org), and the web services called by them. 

Such visualization will allow quality assessment of test-automation scripts being developed for web applications.

The tool was designed and developed during Fall 2020-Spring 2021, as part of a Final-Year capstone engineering project in Queen's University Belfast, UK. 

GaugeDependExtended has been built on top of an earlier tool, named [GaugeDepend](https://github.com/vgarousi/GaugeDepend), which was also developed in our team, back in Spring 2020. Thus, it is the "extended" version of that earlier tool.

# What need does GaugeDependExtended address? / Why should one use this tool?

Software testing is an industry standard for web developers and software engineers. When developing a web application, engineers have found that the test code often has errors and inefficiencies. To help prevent this, continual quality assessment and maintenance is necessary to ensure that the tests are repeatable, predictable, and efficiently executed.  

The visualisation of client-side and server-side test dependencies will allow software test engineers to conduct dependency analysis and assist with quality assessment and maintenance of the test suites.

Here is an example graph generated by GaugeDependExtended for the open-source [PetClinic web application](https://github.com/spring-projects/spring-petclinic):
![Example graph](https://raw.githubusercontent.com/vgarousi/GaugeDependExtended/6d952e23a06fb498748967971a40b9679e82b9f6/resources/petclinic_graph.JPG)

# Development team 
* [Cameron Brush](https://www.linkedin.com/in/cameronbrush/): Cameron worked on the project as his Final-Year capstone engineering project in Queen's University Belfast, UK
* (Project's technical supervisor) [Dr. Vahid Garousi](https://www.vgarousi.com): Professor of Software Engineering in Queen's University Belfast; and Managing Consultant of Bahar Software Engineering Consulting Corporation, UK

# Demo videos
## An overview of the features and code-base of the tool

<a href="http://www.youtube.com/watch?feature=player_embedded&v=Yg9K33ur63o" target="_blank"><img src="http://img.youtube.com/vi/Yg9K33ur63o/0.jpg" 
 width="240" height="180" border="10" /></a>
 
# Documentation

[Here is a 34-page technical report (PDF file)](https://github.com/vgarousi/GaugeDependExtended/blob/362b03e349e287c94949ba1ae78f37d832d97318/docs/Technical%20Report-GaugeDependExtended-May%2019.pdf) which documents the important design aspects of the tool.


# Usge and installation steps:

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


This project is an extension of [GaugeDepend](https://github.com/vgarousi/GaugeDepend) .
---------------------------------------------------------------------------------------------------------
