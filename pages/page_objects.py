from selenium import webdriver
from file import ref
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


# from web_config import Driver


class GuestShopper:

    def __init__(self):
        self.site = webdriver.Chrome()

    def set_up(self):
        self.site.get(ref.url)
        self.site.maximize_window()

    def search_item(self):
        self.site.find_element_by_css_selector(ref.search_box).send_keys(ref.search_item)

    def click_search_button(self):
        self.site.find_element_by_css_selector(ref.search_button).click()

    def select_item(self):
        self.site.find_element_by_css_selector(ref.item).click()

    def add_to_cart(self):
        wait = WebDriverWait(self.site, 15)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ref.add_to_cart_button)))
        self.site.find_element_by_css_selector(ref.add_to_cart_button).click()

    def view_cart_checkout(self):
        wait = WebDriverWait(self.site, 5)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ref.view_cart_checkout)))
        self.site.find_element_by_css_selector(ref.view_cart_checkout).click()

    def proceed_to_checkout(self):
        self.site.find_element_by_css_selector(ref.checkout_button).click()

    def verify_page(self):
        title = self.site.title


    #
    # def click_trip_dropdown(self):
    #     WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located((By.CSS_SELECTOR, labels.trip_drp)))
    #     self.driver.find_element_by_css_selector(labels.trip_drp).click()




    # def verify_page(self, word):
    #     title = self.site.title
    #
    #     try:
    #         assert word in title
    #         print('Assertion Passed')
    #     except AssertionError:
    #         "Text not Found"
    #         print('Assertion Failed')
        # self.site.quit()
