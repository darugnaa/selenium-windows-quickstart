import unittest
import logging
from selenium import webdriver

log = logging.getLogger(__name__)

CHROME_DRIVER_PATH = 'C:/Users/ale/tools/chromedriver.exe'


class ChromeTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.driver.implicitly_wait(5)
        self.driver.get('http://seleniumhq.org/')

    def test_browseSite(self):
        vers = self.driver.capabilities.get('version')
        log.info('--- CHROME %s ---', str(vers))
        news = self.driver.find_elements_by_xpath("//div[@id='mainContent']/ul/li")
        log.info('We have a total of %s news', len(news))
        for n in news:
            log.info(n.text)

    def tearDown(self):
        self.driver.close()
