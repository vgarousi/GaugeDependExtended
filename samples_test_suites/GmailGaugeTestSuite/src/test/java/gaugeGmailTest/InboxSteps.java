package gaugeGmailTest;

import static driver.Driver.wait;
import static org.assertj.core.api.Assertions.assertThat;

import com.thoughtworks.gauge.Step;
import driver.Driver;
import java.io.IOException;
import java.security.GeneralSecurityException;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import util.gmailClient;

public class InboxSteps extends BaseSteps {

  @Step("email appears in inbox")
  public void emailAppears() throws InterruptedException {
    Driver.webDriver.navigate().refresh();
    Thread.sleep(1000);
    assertThat(testMailId).doesNotContainOnlyWhitespaces();
    assertThat(Driver.webDriver.getPageSource().contains(testMailId)).isTrue();
  }

  @Step("click select all")
  public void clickSelectAll() throws InterruptedException {
    WebElement selectAllBtn = (WebElement) wait
        .until(ExpectedConditions.elementToBeClickable(By.cssSelector("[aria-label=\"Select\"]")));
    selectAllBtn.click();
  }

  @Step("click mark as read")
  public void clickMarkAsRead() {
    WebElement btn = (WebElement) wait.until(ExpectedConditions
        .visibilityOfElementLocated(By.cssSelector("[aria-label=\"Mark as read\"]")));
    btn.click();
  }

  @Step("click delete")
  public void clickDelete() {
    WebElement btn = Driver.webDriver.findElement(By.cssSelector("[aria-label=\"Delete\"]"));
    btn.click();
  }

  @Step("Number of emails in inbox is <number>")
  public void numberOfEmailInInbox(int expected)
      throws IOException, GeneralSecurityException, InterruptedException {
    Thread.sleep(4000);
    assertThat(gmailClient.getInboxMessages()).isEqualTo(expected);
  }
}