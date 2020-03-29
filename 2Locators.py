
from selenium import webdriver

from selenium.webdriver import support
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select

# from selenium.webdriversupport.select.Select
driver=webdriver.Firefox(executable_path="/Users/shivanigambhir/Downloads/geckodriver 4")

#driver = webdriver.Chrome(executable_path="/Users/shivanigambhir/Downloads/chromedriver 8.51.34 PM")
driver.get("https://www.rahulshettyacademy.com/angularpractice/")

#driver.find_element_by_name("name").send_keys("Shivani")

driver.find_element_by_css_selector("input[name='name']").send_keys("Shivani")

driver.find_element_by_name("email").send_keys("Shivani.gambhir08@gmail.com")

driver.find_element_by_id("exampleInputPassword1").send_keys("123")

driver.find_element_by_id("exampleCheck1").click()

#how to handel dropdowm > for STATIC > select class provide the method to handle the options in dropdown

driver.maximize_window()

dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))  # ready to handle dropdown3
#dropdown.select_by_visible_text("Female")
dropdown.select_by_index(1)
#dropdown.select_by_value("Female")



driver.find_element_by_xpath("//input[@type='submit']").click()

print(driver.find_element_by_class_name("alert-success").text) # test is to see and comapre message displayed on# screen

message = driver.find_element_by_class_name("alert-success").text
assert "success" in message

#//*[contains(@class,'alert-success')]  -- Xpath

#[class*='alert-success']   -CSS locator

