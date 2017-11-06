import unittest
from selenium import webdriver
from ddt import ddt, data


@ddt
class RegistrationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://demoqa.com/registration/")

    @data(["", "Bobkov", 1, "999999999999", "cat", "av@mail.ru", "qwerty11", "qwerty11"],
          ["Kate", "", 1, "999999999999", "cat", "av@mail.ru", "qwerty11", "qwerty11"],
          ["Matvey12", "111111=+", 0, "mynomber", "friend", "312@g.r", "12noterdam12", "depari1313"],
          ["Kate", "Bobkova", 1, "", "cat", "av@mail.ru", "qwerty11", "qwerty11"],
          ["Kate", "Bobkova", 1, "98759654", "", "av@mail.ru", "qwerty11", "qwerty11"],
          ["Kate", "Bobkova", 1, "675432", "cat", "", "qwerty11", "qwerty11"],
          ["Kate", "Bobkova", 1, "123658778067", "cat", "av@mail.ru", "", "qwerty11"],
          ["Kate", "Bobkova", 1, "111111111", "cat", "av@mail.ru", "qwerty11", ""],
          ["", "", 0, "", "", "", "", ""])
    def test_at_least_one_required_field_is_empty(self, value):
        list_id_elements = ["name_3_firstname", "name_3_lastname", "hobby", "phone_9",
                            "username", "email_1", "password_2", "confirm_password_password_2"]
        for element, val in list(zip(list_id_elements, value)):
            if element is "hobby":
                if val is not 0:
                    self.driver.find_element_by_xpath("//*[@id='pie_register']/li[3]/div/div/input[{0}]".format(val)).click()
            else :
                self.driver.find_element_by_id(element).send_keys(val)

        submit_btn = self.driver.find_element_by_name("pie_submit")
        submit_btn.submit()
        elements_list = self.driver.find_elements_by_css_selector(".legend.error")

        required_field_is_empty=False
        for element in elements_list:
            if element.text=="* This field is required":
                required_field_is_empty=True
                break
        self.assertTrue(required_field_is_empty)

    @data(["qwerty11","qwerty22"], ["qwerty11","1"])
    def test_passwords_match(self, value):
        password_field = self.driver.find_element_by_id("password_2")
        password_confirm_field = self.driver.find_element_by_id("confirm_password_password_2")
        password_field.send_keys(value[0])
        password_confirm_field.send_keys(value[1])
        submit_btn = self.driver.find_element_by_name("pie_submit")
        submit_btn.submit()
        try:
            field=self.driver.find_element_by_xpath("//*[@id='pie_register']/li[12]/div/div/span")
            self.assertEqual("* Fields do not match", field.text)
        except:
            self.assertTrue(False)

    def tearDown(self):
        self.driver.quit()
        pass


if __name__ == "__main__":
    unittest.main()