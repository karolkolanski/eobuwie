# Import bibliotek
from selenium import webdriver
import unittest

class TestRegistration(unittest.TestCase):
    def setUp(self):
        # Przygotowanie testu
        # Otwarta strona https://www.eobuwie.com.pl/
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://www.eobuwie.com.pl/")

    def tearDown(self):
        # Zakończenie testu
        self.driver.quit()

    def testInvalidEmail(self):
        pass

# Jeśli uruchamiam ten plik
if __name__ == "__main__":
    # Uruchom testy
    unittest.main()