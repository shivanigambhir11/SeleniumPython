#JSE DOM can access any elemenrts on web page just like how selenium does
# selenium have a method to execute javascript code in it

# let's ee how to access elements with DOM and using selenium

from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/shivanigambhir/Downloads/chromedriver 8.51.34 PM")
driver.get("https://www.rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").send_keys("Hello")  # hello went into textbox
print (driver.find_element_by_name("name").text)    # i did not get the text i entered in text box "Hello", Whatever user enters
                                                    # we cannot get that by this method
print (driver.find_element_by_name("name").get_attribute("value")) # javascript method get attribute value will get the value, still
                                                                    # using bit of selenium - 1 way
#Use javascript method to get value
print (driver.execute_script('return document.getElementsByName("name")[0].value'))  # pure javascrit > tested in console

shopButton = driver.find_element_by_link_text("Shop")  # In course he used CSS locator but i used
driver.execute_script("arguments[0].click();",shopButton) # Two parameters, 2. locator/variable - what you target, 1. arguments- if teher
                                                        # are 3 variable all will be soted in 1 i.i. why you have to give index and . action;
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")  # Vertical scroll from Top to bottom using Javascript, as selenium cannot scroll on pages






