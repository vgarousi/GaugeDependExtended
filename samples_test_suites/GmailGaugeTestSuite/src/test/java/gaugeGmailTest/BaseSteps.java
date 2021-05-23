package gaugeGmailTest;

import static org.assertj.core.api.Assertions.assertThat;

import com.thoughtworks.gauge.Step;
import driver.Driver;
import java.io.IOException;
import java.security.GeneralSecurityException;
import java.util.UUID;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import util.gmailClient;

public class BaseSteps {

  static String emailAddress;

  static String password;

  static int sentMsgs;

  static String testMailId;

  static int unreadEmails;

  @Step("Go to Gmail Sign in page")
  public void goToGmailHomepage() {
    String gmail_url = "https://www.gmail.com";
    Driver.webDriver.get(gmail_url);
  }

  @Step("Gmail inbox is displayed")
  public void gmailHomepageIsDisplayed() throws InterruptedException {
    boolean actualTitleEquals = (boolean) Driver.wait
        .until(ExpectedConditions.titleContains(emailAddress));
    assertThat(actualTitleEquals).isTrue();
  }

  @Step("Choose account page is shown")
  public void chooseAccPageShown() throws InterruptedException {
    boolean loggedOut = (boolean) Driver.wait
        .until(ExpectedConditions.urlContains("/ServiceLogin/signinchooser"));
    assertThat(loggedOut).isTrue();
  }

  @Step("test user email is: <email>")
  public void setEmail(String email) {
    emailAddress = email;
  }

  @Step("test user password is: <password>")
  public void setPassword(String _password) {
    password = _password;
  }

  public void errorMsgShown(String msgClass) throws InterruptedException {
    WebElement errorMsg = (WebElement) Driver.wait
        .until(ExpectedConditions.visibilityOfElementLocated(By.cssSelector(msgClass)));
    assertThat(errorMsg.isDisplayed()).isTrue();
  }

  @Step("<type> error message is displayed")
  public void errorMsgShownForType(String type) throws InterruptedException {
    switch (type) {
      case "Password":
        errorMsgShown(".EjBTad");
        break;
      case "Email":
        errorMsgShown(".o6cuMc");
        break;
      case "Recipient":
        errorMsgShown(".Kj-JD");
        assertThat(
            Driver.webDriver.getPageSource().contains("Please specify at least one recipient"))
            .isTrue();
        break;
      default:
        break;
    }
  }

  @Step("mark all messages as read")
  public void markAllAsRead() throws IOException, GeneralSecurityException {
    gmailClient.allMessagesMarkedAsRead();
  }

  @Step("number of unread emails is <number>")
  public void numberOfUnreadEmails(int expectedNumber)
      throws GeneralSecurityException, IOException, InterruptedException {
    Thread.sleep(3000);
    assertThat(gmailClient.getUnreadMessages()).isEqualTo(expectedNumber);
  }

  @Step("number of unread emails is increased by 1")
  public void numberOfUnreadIncreasedByOne()
      throws GeneralSecurityException, IOException, InterruptedException {
    Thread.sleep(2000);
    assertThat(gmailClient.getUnreadMessages()).isEqualTo(unreadEmails + 1);
  }

  @Step("number of unread emails is known")
  public void setUnreadEmails() throws GeneralSecurityException, IOException, InterruptedException {
    Thread.sleep(2000);
    unreadEmails = gmailClient.getUnreadMessages();
  }

  @Step("user receives email")
  public void sendEmail() throws Exception {
    testMailId = UUID.randomUUID().toString();
    gmailClient.sendMail("Test mail " + testMailId, "Test email");
  }

  @Step("User has multiple unread emails")
  public void sendMultipleEmails() throws Exception {
    for (int i = 0; i < 5; i++) {
      gmailClient.sendMail("Mark all as read test " + 1, "blah blah blah");
    }
  }

  @Step("click ok")
  public void clickOk() {
    WebElement btn = (WebElement) Driver.wait
        .until(ExpectedConditions.elementToBeClickable(By.name("ok")));
    btn.click();
    try {
      Thread.sleep(1000);
    } catch (InterruptedException x) {
    }
  }
}