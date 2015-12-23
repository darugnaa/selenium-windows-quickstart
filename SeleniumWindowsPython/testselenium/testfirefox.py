import unittest
import logging
from selenium import webdriver

log = logging.getLogger(__name__)

class FirefoxTestCase(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver.manage.timeouts().
        self.driver.get('http://seleniumhq.org/')

    def test_browseSite(self):
        news = self.driver.find_elements_by()
