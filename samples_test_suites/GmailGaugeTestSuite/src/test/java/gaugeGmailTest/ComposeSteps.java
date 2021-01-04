package gaugeGmailTest;

import static org.assertj.core.api.Assertions.assertThat;

import com.thoughtworks.gauge.Step;
import driver.Driver;
import java.io.IOException;
import java.security.GeneralSecurityException;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import util.gmailClient;

public class ComposeSteps extends BaseSteps {

  @Step("number of sent messages is known")
  public void setSentMsgs() throws GeneralSecurityException, IOException {
    sentMsgs = gmailClient.getSentMessages();
  }

  @Step("click compose")
  public void clickCompose() throws InterruptedException {
    WebElement composeBtn = Driver.webDriver.findElement(By.cssSelector(".T-I.J-J5-Ji.T-I-KE.L3"));
    composeBtn.click();
    Thread.sleep(2000);
  }

  @Step("enter <email> in recipients box")
  public void enterRecipient(String email) throws InterruptedException {
    if (email.equals("None")) {
      return;
    }
    WebElement recipientBox = Driver.webDriver.findElement(By.cssSelector("textarea[name=\"to\"]"));
    recipientBox.sendKeys(email);
    Thread.sleep(2000);
  }

  @Step("enter <subject> in subject box")
  public void enterSubject(String subject) throws InterruptedException {
    if (subject.equals("None")) {
      return;
    }
    WebElement subjectBox = Driver.webDriver
        .findElement(By.cssSelector("input[name=\"subjectbox\"]"));
    subjectBox.sendKeys(subject);
    Thread.sleep(2000);
  }

  @Step("enter <body> as message body")
  public void enterMessageBody(String body) throws InterruptedException {
    if (body.equals("None")) {
      return;
    }
    WebElement messageBody = Driver.webDriver
        .findElement(By.cssSelector(".Am.Al.editable.LW-avf.tS-tW"));
    messageBody.sendKeys(body);
    Thread.sleep(2000);
  }

  @Step("click send")
  public void clickSend() throws InterruptedException {
    // T-I J-J5-Ji aoO v7 T-I-atl L3
    WebElement sendBtn = (WebElement) Driver.wait.until(
        ExpectedConditions.elementToBeClickable(By.cssSelector(".T-I.J-J5-Ji.aoO.v7.T-I-atl.L3")));
    sendBtn.click();
  }

  @Step("number of sent messages increased by one")
  public void implementation3() throws GeneralSecurityException, IOException {
    assertThat(gmailClient.getSentMessages()).isEqualTo(sentMsgs + 1);
  }
}