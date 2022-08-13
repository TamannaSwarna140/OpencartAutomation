from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class Registration():
    def register(self):

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get('https://demo.opencart.com/index.php?route=account/register&language=en-gb')

        time.sleep(2)

        first_name = driver.find_element(By.ID, 'input-firstname')
        last_name = driver.find_element(By.ID, 'input-lastname')
        email = driver.find_element(By.ID, 'input-email')
        password = driver.find_element(By.ID, 'input-password')
        subscribe = driver.find_element(By.ID, 'input-newsletter-yes')
        agreement = driver.find_element(By.NAME, 'agree')
        continue_button = driver.find_element(By.XPATH, '//*[@id="form-register"]/div/div/button')

        first_name.send_keys('Sourov')
        time.sleep(2)
        last_name.send_keys('Ahmed')
        time.sleep(2)
        email.send_keys('ssss@gmail.com')
        time.sleep(2)
        password.send_keys('121212')
        time.sleep(2)
        subscribe.click()
        time.sleep(2)
        agreement.click()
        time.sleep(2)
        continue_button.click()
        time.sleep(5)

        driver.close()


obj = Registration()
obj.register()