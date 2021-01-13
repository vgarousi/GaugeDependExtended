# Home Systematic
Created by Cameron on 25/11/2020

This is an exexutable specification file which follows markdown syntax
Every Heading denotes a test. Every bulleted point denotes a step
.....................................................................

There are 4 types of test cases:
    1-Transition from the current node (webpage) to the neighboring nodes (webpages)
    2-Node tp itself (Like form validation)
    3-Input UI tests (in single node/page/unit level)
    4-End to end testing

I will activily use the flow-diagram of web pages for test-case design
.......................................................................
Counts for this spec file:

Node-2-node = 3

Total = 4
........................................................................
##Home page Pre Condition
*Go to Homepage
*Is the current url the same as "http://localhost:8080/"

## Node-2-Node = 1: Find Owners
* Click the Find Owners button
* Is the current url the same as "http://localhost:8080/owners/find"
* Is Find Owners title present

## Node-2-Node = 2: Find Veterinarians
* Click the Veterinarians button
* Is the current url the same as "http://localhost:8080/vets.html"
* Is Veterinarians title present

## Node-2-Node = 3: Find Error
* Click the Error button
* Is the current url the same as "http://localhost:8080/oups"
* Is Error title present

