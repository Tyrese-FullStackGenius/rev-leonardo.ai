import json
import random

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class HeadlessSaver:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)

    def select_account(self):
        with open('config.json') as file:
            data = json.load(file)

        random_account = random.choice(data['bot_accounts'])

        return {
            "username": random_account['email_address'],
            "password": random_account['password'],
        }

    def confirm_account_is_good(self):
        try:
            initial_url = "https://app.leonardo.ai/auth/login"
            self.driver.get(initial_url)
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "chakra-button"))
            )
            button.click()
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(
                EC.presence_of_element_located((By.ID, "signInFormUsername"))
            )
            account_data = self.select_account()
            self.driver.find_element(By.ID, "signInFormUsername").send_keys(account_data['username'])
            self.driver.find_element(By.ID, "signInFormPassword").send_keys(account_data['password'])
            self.driver.find_element(By.NAME, "signInSubmitButton").click()
            wait.until(
                EC.url_contains("https://app.leonardo.ai/")
            ) 
            session_url = "https://app.leonardo.ai/api/auth/session"
            self.driver.get(session_url)
            page_html = self.driver.page_source
            soup = BeautifulSoup(page_html, "html.parser")
            text = soup.get_text()
            parsed_data = json.loads(text)
            sub = parsed_data['user']['sub']
            access = parsed_data['accessToken']
            return {
                        "access_token": access,
                        "sub_id": sub,
                    }
        except Exception as e:
            return str(e)
        finally:
            self.driver.quit()