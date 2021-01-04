# Find Owner Systematic
Created by Cameron on 7/12/2020

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
Node-2-itself = 1

Total = 4
........................................................................

## Node-2-node = 1: View Owners
* Go to Find Owners
* Click the Find Owner button
* Is View Owners title present

## Node-2-node = 2: Click Add Owner
* Go to Find Owners
* Click the Add Owner button
* Is the current url the same as "http://localhost:8080/owners/new"
* Is Owner title present

## Node-2-node = 3: Correct Search
* Go to Find Owners
* Enter "Black"
* Click the Find Owner button
* Is the current url the same as "http://localhost:8080/owners/7"
* Is Owner Information title present

## Node-2-itself = 1: Incorrect Search
* Go to Find Owners
* Enter "lkjh"
* Click the Find Owner button
* Verify error text is shown

