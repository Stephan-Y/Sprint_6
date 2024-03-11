from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_current_element(self, locator):
        return self.driver.find_element(*locator)

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    def find_several_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    def send_keys_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)

    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_element_until_visible(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))

    def get_url(self):
        return self.driver.current_url

    def transfer_on_last_open_window(self):
        handles = self.driver.window_handles
        last_handle = handles[-1]
        self.driver.switch_to.window(last_handle)

    def wait_for_new_window(self, url):
        WebDriverWait(self.driver, 5).until(EC.url_to_be(url))

