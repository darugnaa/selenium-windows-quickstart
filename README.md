# selenium-windows-quickstart
Simple quickstart project to run Selenium on Windows using multiple browsers!


## Versions
Tested on
* Windows 7 x64
* Java binding
  * Java 8 (JDK 1.8.0_65)
  * Maven 3.3.3
  * Selenium 2.48.2
  * TestNG 6.9.9
* Browsers
  * Chrome 47 with [Chromedriver 2.20](http://chromedriver.storage.googleapis.com/2.20/chromedriver_win32.zip)
  * Firefox 42
  * HtmlUnit 2.18
  * Internet Explorer 11 with [IEDriverServer 2.48](http://selenium-release.storage.googleapis.com/2.48/IEDriverServer_x64_2.48.0.zip)
  * Opera 33 with [Operadriver 0.2.2](https://github.com/operasoftware/operachromiumdriver/releases/download/v0.2.2/operadriver_win64.zip)

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

## Run using Python bindings
You need to install selenium in your system or virtualenv. It is available on pypi so you can install it with

    pip install selenium==2.48.0
