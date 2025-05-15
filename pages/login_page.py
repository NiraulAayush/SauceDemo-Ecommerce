from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SauceDemo:
    def __init__(self, driver):
        self.driver =driver
        self.wait = WebDriverWait(driver, 10)
        self.username_id = "user-name"
        self.password_id = "password"
        self.login_btn_id = "login-button"
        self.add_to_cart_id = "add-to-cart-sauce-labs-backpack"
        self.cart_id = "shopping_cart_container"
        self.checkout_id = "checkout"
        self.fname_id  = "first-name"
        self.lname_id = "last-name"
        self.zip_code_id = "postal-code"
        self.continue_id = "continue"
        self.finish_id = "finish"

    def load(self, url):
        self.driver.get(url)

    def login(self, username, password):
        self.wait.until(
            EC.presence_of_element_located((By.ID, self.username_id))
        ).send_keys(username)

        self.wait.until(
            EC.presence_of_element_located((By.ID, self.password_id))
        ).send_keys(password)

        self.wait.until(
            EC.presence_of_element_located((By.ID, self.login_btn_id))
        ).click()

    def cart(self):

        self.wait.until(
            EC.presence_of_element_located((By.ID, self.add_to_cart_id))
        ).click()

        self.wait.until(
            EC.presence_of_element_located((By.ID, self.cart_id))
        ).click()

        self.wait.until(
            EC.presence_of_element_located((By.ID, self.checkout_id))
        ).click()

    def fill_payment_info(self, fname, lname, zip):

        self.wait.until(
            EC.presence_of_element_located((By.ID, self.fname_id))
        ).send_keys(fname)

        self.wait.until(
            EC.presence_of_element_located((By.ID, self.lname_id))
        ).send_keys(lname)

        self.wait.until(
            EC.presence_of_element_located((By.ID, self.zip_code_id))
        ).send_keys(zip)

    def proceed_to_checkout(self):
        self.wait.until(
            EC.presence_of_element_located((By.ID, self.continue_id))
        ).click()

        self.wait.until(
            EC.presence_of_element_located((By.ID, self.finish_id))
        ).click()
