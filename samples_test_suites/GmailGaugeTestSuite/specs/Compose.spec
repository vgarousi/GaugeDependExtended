# Gmail Compse email tests

// Node-2-node
## User sends email
// Arrange
* log in
* number of sent messages is known
// Act.
* Compose email with Recipient:"cboyle51.test@gmail.com", Subject:"test message" Body:"This is a test please ignore"
// Assert
* number of sent messages increased by one
// teardown
* log out

//Node-2-self
## User tries to send mail without recipient
// Arrange
* log in
// Act.
* Compose email with Recipient:"None", Subject:"test message" Body:"This is a test please ignore"
// Assert.
* "Recipient" error message is displayed
// teardown
* click ok
* log out