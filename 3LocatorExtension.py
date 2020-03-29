

from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/shivanigambhir/Downloads/chromedriver 8.51.34 PM")

driver.get("https://login.salesforce.com/")

driver.find_element_by_css_selector("#username").send_keys("Shivani") #generated css with id

driver.find_element_by_css_selector(".password").send_keys("123")  #generated css locator using class name

driver.find_element_by_css_selector(".password").clear()

driver.find_element_by_link_text("Forgot Your Password?").click()  # LInktext locator

driver.find_element_by_xpath("//a[text()='Cancel']").click()  #Xpath based on text //tagname[text()='xxxxx']

#print (driver.find_element_by_xpath("//form[@name ='login]/div[1]/label").text)  #printing username label

print (driver.find_element_by_css_selector("form [name ='login'] label:nth-child(3)").text) # prinint password through grandparent using CSS




