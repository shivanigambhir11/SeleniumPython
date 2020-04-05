

from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome(executable_path="/Users/shivanigambhir/Downloads/chromedriver 8.51.34 PM")
driver.get("https://www.rahulshettyacademy.com/angularpractice/")

driver.find_element_by_link_text("Shop").click()
products = driver.find_elements_by_xpath("//div[@class = 'card h-100']")   # Full 4 phones details


for product in products:
    productName = product.find_element_by_xpath("div/h4/a").text     # Tittle of phone's
    if productName == "Blackberry":
        product.find_element_by_xpath("div/button").click()

driver.find_element_by_xpath("//a[@class ='nav-link btn btn-primary']").click()  # click on Add button of blackberry
#assert product.find_element_by_xpath("div/button") ==  driver.find_element_by_link_text("div/h4/a")
driver.find_element_by_xpath("//button[@class = 'btn btn-success']").click()  #click on checkout button
driver.find_element_by_id("country").send_keys("Ind")  # enter IND in auto suggestive text box

#Explicit Wait
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element_by_link_text("India").click()


driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()  # checkbox check
driver.find_element_by_css_selector("[type='submit']").click()                     # Click Submit
print (driver.find_element_by_class_name("alert-success").text)                    # Check message displayed

successText = driver.find_element_by_class_name("alert-success").text

assert "Success! Thank you!" in successText                                         #assert message

#TAKE SCREENSHOT

driver.get_screenshot_as_file("image.png")







