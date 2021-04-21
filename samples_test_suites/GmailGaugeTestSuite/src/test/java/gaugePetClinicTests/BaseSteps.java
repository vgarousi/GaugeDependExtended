package gaugePetClinicTests;

import static driver.Driver.wait;
import static driver.Driver.webDriver;
import static org.assertj.core.api.Assertions.assertThat;

import com.thoughtworks.gauge.Step;
import driver.Driver;
import gaugePetClinicTests.helpers.ElementHelper;
import gaugePetClinicTests.helpers.StoreHelper;
import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.function.Function;

public class BaseSteps {

	private Logger logger = LoggerFactory.getLogger(getClass());


	@Step("Go to <url>")
	public  void goTopage(String url){
		Driver.webDriver.get(url);
	}

	@Step("Is the current url the same as <url>")
	public boolean isCurrentURLHome(String url) {
		if (url == webDriver.getCurrentUrl()) {
			return true;
		}
		return false;
	}

	@Step("check the <buttonName> is visible <timeout>")
	public boolean checkButtonVisible(String buttonName, long timeout) {
		try {
			Driver.wait.until((Function) ExpectedConditions.visibilityOfElementLocated(getBy(buttonName)));
			return true;
		}
		catch (Exception e) {
			;
			logger.info("Element is not visible");
			return false;
		}
	}

	@Step("focus on element <buttonName>")
	public void focusOnElement(String buttonName) {
		WebElement webElement = webDriver.findElement(getBy(buttonName));
		JavascriptExecutor jse;
		jse = ((JavascriptExecutor) webDriver);
		jse.executeScript("arguments[0].scrollIntoView();", webElement);
		jse.executeScript("arguments[0].focus();", webElement);
	}

	@Step("Check the <buttonName> is clickable <timeout>")
	public boolean checkButtonIsClickable(String buttonName, long timeout) {
		try {
			Driver.wait.until((Function) ExpectedConditions.elementToBeClickable(getBy(buttonName)));
			return true;
		}
		catch (Exception e) {
			logger.info("Element is not visible");
			return false;
		}
	}

	@Step("Click on <buttonName> element")
	public void ClickOnButton(String buttonName) {
		webDriver.findElement(getBy(buttonName)).click();
		logger.info("Element was clicked");
	}


	public By getBy(String key) {
		return ElementHelper.getElementInfoToBy(StoreHelper.INSTANCE.findElementInfoByKey(key));

	}

}
