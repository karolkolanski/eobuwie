# Import bibliotek
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# DANE TESTOWE:
valid_name = "Marcin"
valid_last_name = "Nowak"
valid_password = "alamakotasfinksa"

invalid_email = "kjdkj.pl"

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
        # Zaakceptuj popup
        accept_btn = driver.find_element(By.XPATH, '//button[@data-testid="permission-popup-accept"]')
        accept_btn.click()
        # 1. Kliknij Zarejestruj
        register_btn = driver.find_element(By.XPATH, '//a[@data-testid="header-register-link"]')
        register_btn.click()
        # Sprawdź, czy otwiera się strona rejestracji
        self.assertIn("Utwórz nowe konto klienta", driver.title)
        # "Czysty" Python
        # assert "Utwórz nowe konto klienta" in driver.title
        # 2. Wpisz imię
        name_input = driver.find_element(By.ID, 'firstname')
        name_input.send_keys(valid_name)
        # 3. Wpisz nazwisko
        last_name_input = driver.find_element(By.ID, 'lastname')
        last_name_input.send_keys(valid_last_name)
        # 4. Wpisz niepoprawy e-mail
        email_input = driver.find_element(By.ID, 'email_address')
        email_input.send_keys(invalid_email)
        # 5. Wpisz hasło
        driver.find_element(By.ID, 'password').send_keys(valid_password)
        # 6. Potwierdź hasło
        driver.find_element(By.ID, 'confirmation').send_keys(valid_password)
        # 7. Zaznacz zgodę na otrzymywanie informacji handlowych od MODIVO S.A
        marketing_checkbox_label = driver.find_element(By.XPATH, '//label[@class="checkbox-wrapper__label account-create__statement-label"]')
        marketing_checkbox_label.click()

        ## Oczekiwany rezultat
        # Użytkownik otrzymuje informację "Wprowadzono niepoprawny adres-email" pojawiającą się pod polem
        # Wyszykuję błędy
        errors = driver.find_elements(By.XPATH, '//span[@class="help-block form-error"]')
        # Sprawdzam, czy jest 1 element w liście errors
        self.assertEqual(1, len(errors))
        # Sprawdź tekst błędu
        self.assertEqual("Wprowadzono niepoprawny adres e-mail", errors[0].text)
        # Kontrolny sleep na końcu -  do usunięcia jak będzie gotowe
        # sleep(3)

# Jeśli uruchamiam ten plik
if __name__ == "__main__":
    # Uruchom testy
    unittest.main()