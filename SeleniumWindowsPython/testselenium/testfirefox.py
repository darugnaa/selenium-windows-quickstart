import unittest
import logging
from selenium import webdriver

log = logging.getLogger(__name__)


class FirefoxTestCase(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.driver.get('http://seleniumhq.org/')

    def test_browseSite(self):
        log.info('--- FIREFOX %s ---', self.driver.capabilities.get('version'))
        news = self.driver.find_elements_by_xpath("//div[@id='mainContent']/ul/li")
        log.info('We have a total of %s news', len(news))
        for n in news:
            log.info(n.text)

    def tearDown(self):
        self.driver.close()
