from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class Opencart():
    def registration_demo(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        driver.get("https://demo.opencart.com/")

        #find_elements

        #my_accounts
        my_accounts = driver.find_element(By.XPATH,'//*[@id="top"]/div[2]/div[2]/ul/li[2]/div/a/i[2]')
        my_accounts.click()
        time.sleep(2)


        #registration
        registration = driver.find_element(By.XPATH,'//*[@id="top"]/div[2]/div[2]/ul/li[2]/div/ul/li[1]/a')
        registration.click()
        time.sleep(2)

        #first_name
        first_name = driver.find_element(By.ID,'input-firstname')
        first_name.send_keys("Tazan")
        time.sleep(2)

        #last_name
        last_name = driver.find_element(By.ID,"input-lastname")
        last_name.send_keys("Rabbani")
        time.sleep(5)

        #Email
        email = driver.find_element(By.ID, "input-email")
        email.send_keys("trjuned2@gmail.com")
        time.sleep(5)

        #password
        password = driver.find_element(By.ID, "input-password")
        password.send_keys("1234567890")
        time.sleep(5)

        #radio_button
        radio_button = driver.find_element(By.XPATH, '//*[@id="form-register"]/fieldset[3]/div/div/div[1]/label')
        radio_button.click()
        time.sleep(2)

        #terms and condition
        privacy_policy = driver.find_element(By.XPATH, '//*[@id="form-register"]/div/div/div/input')
        privacy_policy.click()
        time.sleep(2)

        #Button
        btn = driver.find_element(By.XPATH, '//*[@id="form-register"]/div/div/button')
        btn.click()
        time.sleep(2)


        print("Sucessfully Registration")

        time.sleep(2)
        driver.close()

obj = Opencart()
obj.registration_demo()




