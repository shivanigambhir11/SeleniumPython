from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/shivanigambhir/Downloads/chromedriver 8.51.34 PM")

driver.get("https://the-internet.herokuapp.com/windows")     # site to practice web autonmation
driver.find_element_by_link_text("Click Here").click()       #using link text to click on "click here"
childwindow= driver.window_handles[1]                        #whuich window we will handle later [0,1,2] means 0 is parent, 1 child, 2 child

driver.switch_to.window(childwindow)                         #to switch to child window , whichone we already mentioned
print(driver.find_element_by_tag_name("h3").text)            #use tag name locator for next page heading as there is on;y 1 tagname & print
driver.close()
driver.switch_to.window(driver.window_handles[0])            #Go back to parent > pass that value in index

assert "Opening a new window" ==driver.find_element_by_tag_name("h3").text            #print value to check if everthing ok
