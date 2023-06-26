import time
from faker import Faker
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class SubmitForm:
    def __init__(self, driver):
        self.driver = driver


    def submit_form(self):
        fake = Faker()
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        # Open the website and maximize the window
        driver.get("https://demoqa.com/automation-practice-form")
        driver.maximize_window()

        print("Test case started")

        name_length = 7

        for i in range(name_length):
            first_name = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'firstName')))
            first_name.send_keys(fake.first_name())

            last_name = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'lastName')))
            last_name.send_keys(fake.last_name())

            user_email = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'userEmail')))
            user_email.send_keys(fake.email())

            gender_radio = driver.find_element(By.XPATH, "//label[contains(text(),'Male')]")
            driver.execute_script('arguments[0].click()', gender_radio)

            user_number = driver.find_element(By.ID, 'userNumber')
            user_number.send_keys(fake.random_int(1000000000, 9999999999))

            dob = driver.find_element(By.ID, 'dateOfBirthInput')
            driver.execute_script('arguments[0].click()', dob)

            # Calendar popup
            select_month = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__month-select"))
            select_month.select_by_index(fake.random_int(0, 11))
            time.sleep(1)

            select_year = Select(driver.find_element(By.CLASS_NAME, "react-datepicker__year-select"))
            select_year.select_by_value(str(fake.random_int(1970, 2000)))
            time.sleep(1)

            select_day = driver.find_element(By.XPATH, "//div[contains(@class, 'react-datepicker__day--0') and not(contains(@class, 'outside'))]")
            driver.execute_script('arguments[0].click()', select_day)

            subject = driver.find_element(By.ID, 'subjectsInput')
            subject.send_keys(fake.random_element(['Computer Science', 'Physics', 'Mathematics', 'Chemistry']))
            subject.send_keys(Keys.RETURN)

            hobbies = driver.find_element(By.XPATH, "//label[contains(text(),'Sports')]")
            driver.execute_script('arguments[0].click()', hobbies)

            upload_pic = driver.find_element(By.ID, 'uploadPicture')
            upload_pic.send_keys("//Users//mac//Downloads//sqa.jpg")

            current_address = driver.find_element(By.ID, 'currentAddress')
            current_address.send_keys(fake.address().replace("\n", ", "))

            driver.execute_script("document.body.style.zoom='50%'")

            current_address.send_keys(Keys.TAB)

            time.sleep(1)

            state_name = driver.find_element(By.ID, 'react-select-3-input')
            state_name.send_keys('Haryana')
            state_name.send_keys(Keys.RETURN)
            state_name.send_keys(Keys.TAB)

            select_city = driver.find_element(By.ID, "react-select-4-input")
            select_city.send_keys(fake.city())
            select_city.send_keys(Keys.RETURN)

            submit_btn = driver.find_element(By.XPATH, "//button[@id='submit']")
            driver.execute_script('arguments[0].click()', submit_btn)

            time.sleep(1)

            close_btn = driver.find_element(By.ID, 'closeLargeModal')
            driver.execute_script('arguments[0].click()', close_btn)

            time.sleep(1)

submit_form= SubmitForm(webdriver)
submit_form.submit_form()