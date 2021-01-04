# Gmail login tests

// Setup Required for each test.
* test user email is: "cameroncbrush@gmail.com"
* test user password is: "Tr1stanb16"

//Node-2-node
// fresh login
## Successful Gmail login
// Arrange.
* Go to Gmail Sign in page
// Act.
* type email address
* type password
// Assert.
* Gmail inbox is displayed
// termdown
* log out

//Node-2-self
## Failed Login - Bad Password
// Arrange.
* Go to Gmail Sign in page
// Act.
* type email address
* user types incorrect password
// Assert.
* "Password" error message is displayed

//Node-2-self
## Failed Login - Incorrect Email address
// Arrage.
* Go to Gmail Sign in page
// Act.
* user types bad email address
// Assert
* "Email" error message is displayed

//
