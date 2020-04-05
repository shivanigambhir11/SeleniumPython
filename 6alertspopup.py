from selenium import webdriver
validatText='Option3'

driver = webdriver.Chrome(executable_path="/Users/shivanigambhir/Downloads/chromedriver 8.51.34 PM")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_css_selector("#name").send_keys(validatText)    #go to textbox and enter Option3  by typing ('Option3')
driver.find_element_by_id("alertbtn").click()            #click alrt button
alert = driver.switch_to.alert   # go to javascript popup, handle with switching option
alertText= alert.text
assert validatText in alertText         #print (alert.text)     # to print text of pop up
alert.accept ()       # click on accept button of pop up also to click on positive scnario
alert.dismiss()       # to click oni negative scenario like cancel/ no
