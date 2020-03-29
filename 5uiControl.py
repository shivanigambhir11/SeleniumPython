
from selenium import webdriver


driver = webdriver.Chrome(executable_path="/Users/shivanigambhir/Downloads/chromedriver 8.51.34 PM")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

# checkboxes= driver.find_elements_by_xpath("//input[@type='checkbox']")
# print (len (checkboxes))
#
# for checkbox in checkboxes:
#     if checkbox.get_attribute("value")=="option2":
#         checkbox.click()
#         assert checkbox.is_selected()    # to check if all checkboxes are checked
#
#
# radiobuttons = driver.find_elements_by_name("radioButton")
# radiobuttons[2].click()
# assert radiobuttons[2].is_selected()

# IS DISPLAYED FUN- HIDE/ SHOW and TEXT box are there > first verify textbox is there > 2 click on hide > 3 verify ioif textbox is there 
assert driver.find_element_by_id("displayed-text").is_displayed()
driver.find_element_by_id("hide-textbox").click()
assert not driver.find_element_by_id("displayed-text").is_displayed()



