# selenium-windows-quickstart
Simple quickstart project to run Selenium on Windows 10 using multiple browsers!


## Versions
Tested on
* Windows 10 Pro 64bit (Build 10586.420)
* Java binding
  * Java 8 (JDK 1.8.0_66)
  * Maven 3.3.3
  * Selenium 2.48.2
  * TestNG 6.9.9
* Browsers
  * Chrome 51 with [Chromedriver 2.22](http://chromedriver.storage.googleapis.com/2.22/chromedriver_win32.zip)
  * Firefox 46
  * HtmlUnit 2.18
  * Edge 25 with [MicrosoftWebDriver 10586](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
  * Opera 38 with [Operadriver 0.2.2](https://github.com/operasoftware/operachromiumdriver/releases/download/v0.2.2/operadriver_win64.zip)

From Firefox 47 the `FirefoxDriver` is discotninued. The new `Marionette` driver is not officially released yet.
You can read more on StackOverflow: [Selenium 2.53 not working on Firefox 47](http://stackoverflow.com/questions/37693106/selenium-2-53-not-working-on-firefox-47),
[Firefox 47.0 to crash on startup selenium webdriver](http://stackoverflow.com/questions/37791436/firefox-47-0-to-crash-on-startup-selenium-webdriver);
and on [MDN](https://developer.mozilla.org/en-US/docs/Mozilla/QA/Marionette/WebDriver).
  
# Setup
Clone this repository into your local machine

    git clone https://github.com/darugnaa/selenium-windows-quickstart.git
    cd selenium-windows-quickstart
    start .

## Driver setup
Download drivers for Chrome, IE and Opera. Unzip them into a folder, for example `C:\Users\you\drivers\`.  
Edit the Java project pom.xml and add the full path in the `<properties>` section.

## Run using Java bindings

    cd SeleniumWindowsJava
    mvn clean verify
