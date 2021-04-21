package gaugePetClinicTests.helpers;

import gaugePetClinicTests.models.ElementInfo;
import org.openqa.selenium.By;

public class ElementHelper {

	public static By getElementInfoToBy(ElementInfo elementInfo) {
		By by = null;
		String elementInfoValue = elementInfo.getValue();
		switch (elementInfo.getType()) {
		case "css":
			by = By.cssSelector(elementInfoValue);
			break;
		case "id":
			by = By.id(elementInfoValue);
			break;
		case "xpath":
			by = By.xpath(elementInfoValue);
			break;
		case "class":
			by = By.className(elementInfoValue);
			break;
		case "linkText":
			by = By.linkText(elementInfoValue);
			break;
		case "name":
			by = By.name(elementInfoValue);
			break;
		case "tag":
			by = By.tagName(elementInfoValue);
			break;
		default:
			throw new NullPointerException("Incorrect Element type");
		}
		return by;
	}

	public static By getElementInfoToBy(String byValue, String selectorType) {

		By by = null;
		String elementInfoValue = byValue;
		switch (selectorType) {
		case "css":
			by = By.cssSelector(elementInfoValue);
			break;
		case "id":
			by = By.id(elementInfoValue);
			break;
		case "xpath":
			by = By.xpath(elementInfoValue);
			break;
		case "class":
			by = By.className(elementInfoValue);
			break;
		case "linkText":
			by = By.linkText(elementInfoValue);
			break;
		case "name":
			by = By.name(elementInfoValue);
			break;
		default:
			throw new NullPointerException("Incorrect Element type");
		}
		return by;
	}

}
