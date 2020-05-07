package gaugeGmailTest;

import static driver.Driver.wait;
import static driver.Driver.webDriver;

import com.thoughtworks.gauge.Step;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;

public class LoginSteps extends BaseSteps {

  public void enterEmail(String email) {
    wait.until(ExpectedConditions.visibilityOfElementLocated(By.name("identifier")));
    webDriver.findElement(By.name("identifier")).sendKeys(email);
    wait.until(ExpectedConditions.elementToBeClickable(By.cssSelector(".RveJvd.snByac")));
    webDriver.findElement(By.cssSelector(".RveJvd.snByac")).click();
  }

  @Step("type email address")
  public void enterCorrectEmail() {
    enterEmail(BaseSteps.emailAddress);
  }

  @Step("user types bad email address")
  public void enterEmailNonExistent() {
    enterEmail("cboyle51.test1234556@gmail.com");
  }

  public void enterPassword(String pass) throws InterruptedException {
    wait.until(ExpectedConditions.visibilityOfElementLocated(By.name("password")));
    webDriver.findElement(By.name("password")).sendKeys(pass);
    wait.until(ExpectedConditions
        .refreshed(ExpectedConditions.elementToBeClickable(By.cssSelector(".RveJvd.snByac"))));
    webDriver.findElement(By.cssSelector(".RveJvd.snByac")).click();
  }

  @Step("type password")
  public void correctPassword() throws InterruptedException {
    //assertThat(webDriver.getPageSource().contains("Wrong password")).isFalse();
    enterPassword(BaseSteps.password);
  }

  @Step("user types incorrect password")
  public void badPassword() throws InterruptedException {
    enterPassword("abc123blahblahblahblahlsdk");
  }

  @Step("log out")
  public void logOut() throws InterruptedException {
    WebElement userBtn = (WebElement) wait
        .until(ExpectedConditions.elementToBeClickable(By.cssSelector(".gb_Ia.gbii")));
    userBtn.click();
    WebElement signOutBtn = (WebElement) wait
        .until(ExpectedConditions.elementToBeClickable(By.linkText("Sign out")));
    signOutBtn.click();
  }
}