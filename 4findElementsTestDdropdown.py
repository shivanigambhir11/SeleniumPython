import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/shivanigambhir/Downloads/chromedriver 8.51.34 PM")

driver.get("https://www.makemytrip.com/")

driver.find_element_by_id("fromCity").click()
driver.find_element_by_css_selector("input[placeholder='From']").send_keys("del")

time.sleep(2)

cities = driver.find_elements_by_css_selector("p[class*='blackText']")  # get all values in drop dropdown

print (len (cities))    # to know lwngth of citites


for city in cities:         # iterate through list cities to print them
    #print (city.text)     # bcz city is just web element, but city text is city name
    if city.text =="Del Rio, United States":  # click on city DelRio
        city.click()
        break  # if our city is on 4/30 cities why we have to go 26more cities lets come out of loop

# now select To location Delhi using simple css locator
driver.find_element_by_xpath("//p[text()='Delhi, India']").click()