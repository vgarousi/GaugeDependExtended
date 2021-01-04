# Owner Information Systematic
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

Node-2-node = 4

Total = 4
........................................................................

## Node-2-itself = 1: View Owner Information
* Go to Owner Information
* Get number of pets
* Check if information table is visible

## Node-2-node = 1: Update Pet
* Go to Owner Information
* Click the Edit Pet button
* Click the Update Button

## Node-2-node = 2: View Find Owners
* Go to Find Owners

## Node-2-node = 3: Add new Pet successfully
* Go to Owner Information
* Click on add new pet
* View new pet page
* Add pet successfully

## Node-2-node = 4: Add new Pet unsuccessfully
* Go to Owner Information
* Click on add new pet
* View new pet page
* Add pet unsuccessfully
* Is the current url the same as "http://localhost:8080/owners/6/pets/new"

