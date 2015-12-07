package org.darugna.selenium.windows.seleniumwindows;

import java.util.List;
import java.util.concurrent.TimeUnit;
import org.openqa.selenium.By;
import org.openqa.selenium.Capabilities;
import org.openqa.selenium.HasCapabilities;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.opera.OperaDriver;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

/**
 *
 * @author Alessandro Da Rugna (alessandro.darugna@gmail.com)
 */
public class OperaTest {

    private WebDriver driver;
    
    @BeforeMethod
    public void setupBrowser() {
        // Download the operadriver executable from  https://github.com/operasoftware/operachromiumdriver/releases/tag/v0.2.2
        driver = new OperaDriver();
        driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
        driver.get("http://docs.seleniumhq.org/");
    }
    
    @Test
    public void browseTheSite() {
        Capabilities c = ((HasCapabilities)driver).getCapabilities();
        System.out.println("--- OPERA " + c.getVersion() + " ---");
        List<WebElement> newsListItem = driver.findElements(By.xpath("//div[@id='mainContent']/ul/li"));
        System.out.println("We have a total of " + newsListItem.size() + " news");
        newsListItem.stream().forEach(news -> System.out.println(news.getText()));
    }

    @AfterMethod
    public void closeBrowser() {
        driver.quit();
    }

}
