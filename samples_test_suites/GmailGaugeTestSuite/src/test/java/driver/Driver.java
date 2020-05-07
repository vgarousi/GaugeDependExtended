package driver;

import com.thoughtworks.gauge.AfterScenario;
import com.thoughtworks.gauge.AfterSuite;
import com.thoughtworks.gauge.BeforeScenario;
import com.thoughtworks.gauge.BeforeSuite;
import java.time.Duration;
import java.util.concurrent.TimeUnit;
import org.openqa.selenium.ElementClickInterceptedException;
import org.openqa.selenium.NoSuchElementException;
import org.openqa.selenium.NoSuchWindowException;
import org.openqa.selenium.StaleElementReferenceException;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.ui.FluentWait;
import org.openqa.selenium.support.ui.Wait;

public class Driver {

    // Holds the WebDriver instance
    public static WebDriver webDriver;
    public static Wait wait;

    // Initialize a webDriver instance of required browser
    // Since this does not have a significance in the application's business domain, the BeforeSuite hook is used to instantiate the webDriver
    @BeforeScenario
    public void initializeDriver(){
        webDriver = DriverFactory.getDriver();
        webDriver.manage().timeouts().implicitlyWait(3, TimeUnit.SECONDS);
        wait = new FluentWait(webDriver)
            .withTimeout(Duration.ofSeconds(15))
            .pollingEvery(Duration.ofMillis(200))
            .ignoring(Exception.class)
            .ignoring(NoSuchWindowException.class)
            .ignoring(NoSuchElementException.class)
            .ignoring(ElementClickInterceptedException.class)
            .ignoring(StaleElementReferenceException.class);
    }

    // Close the webDriver instance
    @AfterScenario
    public void closeDriver(){
        webDriver.quit();
    }

}
