package gaugePetClinicTests;

import com.thoughtworks.gauge.Step;

import static driver.Driver.wait;
import static driver.Driver.webDriver;
import static org.assertj.core.api.Assertions.assertThat;

import driver.Driver;
import gaugePetClinicTests.helpers.ElementHelper;
import gaugePetClinicTests.helpers.StoreHelper;
import org.openqa.selenium.*;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.openqa.selenium.By;

import java.util.function.Function;

public class HomeSteps {

    @Step("check for <title> with <text>")
    public void isTitlePresent(String title, String text){
        Boolean correctTitle = (boolean) wait.until(ExpectedConditions.textToBe(getBy(title),text));
        assertThat(correctTitle).isTrue();
    }

    public By getBy(String key) {
        return ElementHelper.getElementInfoToBy(StoreHelper.INSTANCE.findElementInfoByKey(key));

    }

}
