# Gmail Inbox tests

//Node-2-self
## User recieves email
// Arrange.
* log in
* number of unread emails is known
// Act.
* user receives email
// Assert.
* number of unread emails is increased by 1
* email appears in inbox
// teardown
* log out
* mark all messages as read

//Node-2-self
## User is able to mark all emails as read
// Arrange.
* User has multiple unread emails
* log in
// Act.
* click select all
* click mark as read
// Assert.
* number of unread emails is "0"
// teardown
* log out

//Node-2-self
## User deletes all emails
// Arrange.
* User has multiple unread emails
* log in
// Act.
* click select all
* click delete
// Assert.
* Number of emails in inbox is "0"
// teardown
* log out

// Node-2-node
## Log out
// Arrange.
* log in
// Act.
* log out
// Assert.
* Choose account page is shown
