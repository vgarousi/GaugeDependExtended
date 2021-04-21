package gaugePetClinicTests;

import static driver.Driver.wait;
import static driver.Driver.webDriver;

import com.thoughtworks.gauge.Step;
import driver.Driver;
import gaugePetClinicTests.helpers.ElementHelper;
import gaugePetClinicTests.helpers.StoreHelper;
import org.openqa.selenium.*;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.openqa.selenium.By;

import java.util.function.Function;
import static org.assertj.core.api.Assertions.assertThat;

public class FindOwnerSteps {


    @Step("Enter <text>")
    public  void enterLastName(String text) throws InterruptedException {
        enterText(text, "lastName");
    }

    @Step("Verify error text is shown")
    public void viewErrorText(){
        Boolean errorMessage = (boolean) wait.until(ExpectedConditions.textToBe(getBy("Error Message"),"has not been found"));
        assertThat(errorMessage).isTrue();
    }

    public By getBy(String key) {
        return ElementHelper.getElementInfoToBy(StoreHelper.INSTANCE.findElementInfoByKey(key));

    }

    public void enterText(String text, String textboxID) throws InterruptedException {
        wait.until(ExpectedConditions.visibilityOfElementLocated(getBy(textboxID)));
        webDriver.findElement(getBy(textboxID)).sendKeys(text);
    }
}
