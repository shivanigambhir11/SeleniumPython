
from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/shivanigambhir/Downloads/chromedriver 8.51.34 PM")
driver.get("https://the-internet.herokuapp.com/iframe")     # go to this site to perform iframes

driver.switch_to.frame("mce_0_ifr")             # before ypu start you have to switch from html to iframe/frame/frameset
driver.find_element_by_xpath("//p[text()='Your content goes here.']").clear()   #clear the text where you want to write
driver.find_element_by_css_selector("#tinymce").send_keys("I will and i am automating this with my locators and not with Rahul's locators")
# Go banck again once that is clear and write down your own message
driver.switch_to.default_content()   #If you wanna come out of frame when you are done switch to normal content

print (driver.find_element_by_tag_name("h3").text)   # write message of that page which is out of frame