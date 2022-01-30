# Import bibliotek
from selenium import webdriver
import unittest

class TestRegistration(unittest.TestCase):
    def setUp(self):
        # Przygotowanie testu
        # Otwarta strona https://www.eobuwie.com.pl/

    def tearDown(self):
        pass
    def testInvalidEmail(self):
        pass

# Jeśli uruchamiam ten plik
if __name__ == "__main__":
    # Uruchom testy
    unittest.main()