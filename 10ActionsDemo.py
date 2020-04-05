from selenium import webdriver
from selenium.webdriver import ActionChains


driver = webdriver.Chrome(executable_path="/Users/shivanigambhir/Downloads/chromedriver 8.51.34 PM")
driver.get("https://www.familysearch.org/en/")

#ActionChains

action = ActionChains(driver)    #Advanced classes will be used name as ActionChains
    action.move_to_element(driver.find_element_by_id("search")).perform()   # this will move you to Search button & perform will hover over that search buutton
    action.move_to_element(driver.find_element_by_link_text("Genealogies")).click().perform()  # will go futher down to genealogies and click

lets (DOUBLE CLICK//CONTEXT CLICK- RiGHT CLICK) and (accept the pop up that appears) also (assert the message) on pop up
    driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
    action.context_click(driver.find_element_by_id("double-click")).perform()
    action.double_click(driver.find_element_by_id("double-click")).perform()

    alert = driver.switch_to.alert
    assert "You double clicked me!!!, You got to be kidding me" ==alert.text
    alert.accept()


#







