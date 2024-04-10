from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
import os
from selenium.webdriver.common.by import By

class WikipediaTests(unittest.TestCase):

    def setUp(self):
        self.path_driver=os.chdir(r'C:\Users\Sebas\Desktop\Itla\Quinto cuatrimestre\Programacion III\tarea')

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.wikipedia.org")
        time.sleep(2) 
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
    def tearDown(self):
        self.driver.quit()

    def take_screenshot(self, name):

        timestamp = time.strftime('%Y%m%d_%H%M%S')
        screenshot_path = os.path.join("screenshots", f"{name}_{timestamp}.png")
        self.driver.save_screenshot(screenshot_path)

    def test_search_term(self):
        search_input = self.driver.find_element(By.ID,"searchInput")
        search_input.send_keys("Python programming language")
        self.take_screenshot("Write in search input")
        search_input.send_keys(Keys.RETURN)
        time.sleep(2) 
        self.take_screenshot("search_term")
        self.assertTrue(self.driver.find_element(By.CLASS_NAME,"mw-search-result-heading").is_displayed())

    def test_access_article_page(self):
        search_input = self.driver.find_element(By.ID,"searchInput")
        search_input.send_keys("Python programming language")
        search_input.send_keys(Keys.RETURN)
        time.sleep(2)  
        article_link = self.driver.find_element(By.CLASS_NAME,"mw-search-result-heading")
        article_link.click()
        self.take_screenshot("access_article_page")
        time.sleep(2) 
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR,".mw-parser-output").is_displayed())

    def test_change_interface_language(self):
        language_link = self.driver.find_element(By.CSS_SELECTOR, "#js-link-box-en > strong")
        self.take_screenshot("test_change_interface_language")
        language_link.click()
        self.take_screenshot("language_changed")
        time.sleep(2)
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, ".lang1").is_displayed())

    def test_exist_image(self):
        search_input = self.driver.find_element(By.ID,"searchInput")
        search_input.send_keys("Python programming language")
        search_input.send_keys(Keys.RETURN)
        time.sleep(2)  
        save_button = self.driver.find_element(By.CLASS_NAME, "mw-file-element")
        self.take_screenshot("test_exist_image")
        self.assertTrue(self.driver.find_element(By.CLASS_NAME, "mw-file-element").is_displayed())
        save_button.click()

    def test_See_Title(self):
        search_input = self.driver.find_element(By.ID,"searchInput")
        search_input.send_keys("Python programming language")
        search_input.send_keys(Keys.RETURN)
        time.sleep(2) 
        self.take_screenshot("test_See_Title")
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, ".firstHeading").is_displayed())


if __name__ == "__main__":
    unittest.main()