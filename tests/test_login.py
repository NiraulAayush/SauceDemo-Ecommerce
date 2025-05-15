from pages.login_page import SauceDemo
from datas import test_data
import time

URL = "https://www.saucedemo.com/"

def test_valid_login(driver):
    #Login
    ecommerce = SauceDemo(driver)
    ecommerce.load(URL)
    ecommerce.login(test_data.valid_credentials["username"], test_data.valid_credentials["password"])

    #Add to Cart
    ecommerce.cart()

    #Fill information
    ecommerce.fill_payment_info(test_data.form_info["firstname"], test_data.form_info["lastname"], test_data.form_info["zipcode"])

    #checkout
    ecommerce.proceed_to_checkout()

    assert "checkout-complete.html" in driver.current_url.lower()