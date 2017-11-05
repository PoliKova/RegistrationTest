import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class RegistrationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://demoqa.com/registration/")

    def test_at_least_one_required_field_is_empty(self):
        self.search_field = self.driver.find_element_by_name("pie_submit")
        self.search_field.submit()
        list = self.driver.find_elements_by_css_selector(".legend.error")

        required_field_is_empty=False
        for element in list:
            if element.text=="* This field is required":
                required_field_is_empty=True
                break

        self.assertTrue(required_field_is_empty)

    def tearDown(self):
        self.driver.quit()
        pass


if __name__ == "__main__":
    unittest.main()