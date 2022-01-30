# Import bibliotek
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


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
        driver = self.driver
        # Kroki:
        # 1. Kliknij Zarejestruj - otwiera się strona rejestracji
        accept_btn = driver.find_element(By.XPATH, '//button[@data-testid="permission-popup-accept"]')
        accept_btn.click()
        # Kontrolny sleep na końcu -  do usunięcia jak będzie gotowe
        sleep(3)

# Jeśli uruchamiam ten plik
if __name__ == "__main__":
    # Uruchom testy
    unittest.main()