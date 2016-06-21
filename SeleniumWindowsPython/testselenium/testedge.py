import unittest
import logging
from selenium import webdriver

log = logging.getLogger(__name__)

EDGE_DRIVER_PATH = 'C:/Program Files (x86)/Microsoft Web Driver/MicrosoftWebDriver.exe'


class ChromeTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge(executable_path=EDGE_DRIVER_PATH)
        self.driver.implicitly_wait(5)
        self.driver.get('http://seleniumhq.org/')

    def test_browseSite(self):
        vers = self.driver.capabilities.get('version')
        log.info('--- EDGE %s ---', str(vers))
        news = self.driver.find_elements_by_xpath("//div[@id='mainContent']/ul/li")
        log.info('We have a total of %s news', len(news))
        for n in news:
            log.info(n.text)

    def tearDown(self):
        self.driver.close()
