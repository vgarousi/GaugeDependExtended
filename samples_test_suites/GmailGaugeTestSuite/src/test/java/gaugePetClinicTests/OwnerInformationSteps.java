package gaugePetClinicTests;

import com.thoughtworks.gauge.Step;

import static driver.Driver.wait;
import static driver.Driver.webDriver;

import gaugePetClinicTests.helpers.ElementHelper;
import gaugePetClinicTests.helpers.StoreHelper;
import org.openqa.selenium.*;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.Select;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.openqa.selenium.By;
import static org.assertj.core.api.Assertions.assertThat;

import java.util.function.Function;

public class OwnerInformationSteps {

    private Logger logger = LoggerFactory.getLogger(getClass());

    @Step("View all owners")
    public void viewAllOwners(){

    }

    @Step("Add pet successfully")
    public void addPetSuccessfully() throws InterruptedException {
        enterText("Tim", "name");
        enterText("2014/5/6", "birthDate");
        Select dropdown = new Select(webDriver.findElement(getBy("type")));
        dropdown.selectByVisibleText("dog");
        webDriver.findElement(getBy("Add Pet")).click();
    }

    @Step("Add pet unsuccessfully")
    public void addPetUnsuccessfully() throws InterruptedException {
        enterText("", "name");
        enterText("", "birthDate");
        webDriver.findElement(getBy("Add Pet")).click();
    }

    @Step("View new pet page")
    public void viewNewPetPage(){
        Boolean correctTitle = (boolean) wait.until(ExpectedConditions.textToBe(getBy("NewPet"),"New Pet"));
        assertThat(correctTitle).isTrue();
    }

    @Step("Get number of pets")
    public void getNumberOfPets(){
        int numberOfPets = webDriver.findElements(getBy("PetRow")).size();
        System.out.println("Number of pets: " + numberOfPets);
        logger.info("Number of pets: " + numberOfPets);

    }

    @Step("Check if information table is visible")
    public void viewInfromationTable(){
        wait.until(ExpectedConditions.visibilityOfElementLocated(getBy("InformationTable")));

    }

    @Step("click on <buttonName> button")
    public void addOwnerButton(String buttonName) {
        wait.until(ExpectedConditions.elementToBeClickable(getBy(buttonName)));
        webDriver.findElement(By.linkText("Add Owner")).click();
    }

    @Step("add owner")
    public void addOwner() throws InterruptedException {
        enterText("Amy", "firstName");
        enterText("Quinn", "lastName");
        enterText("123 MadeUp Street", "address");
        enterText("Banbridge", "city");
        enterText("12345678", "telephone");
        wait.until(ExpectedConditions.elementToBeClickable(By.cssSelector("button.btn.btn-default")));
        webDriver.findElement(By.cssSelector("button.btn.btn-default")).click();

    }

    public void enterText(String text, String textboxID) throws InterruptedException {
        wait.until(ExpectedConditions.visibilityOfElementLocated(getBy(textboxID)));
        webDriver.findElement(getBy(textboxID)).sendKeys(text);
    }

    public By getBy(String key) {
        return ElementHelper.getElementInfoToBy(StoreHelper.INSTANCE.findElementInfoByKey(key));

    }
}
