
from selenium import webdriver
from selenium.webdriver.support.select import Select

# from selenium.webdriversupport.select.Select

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized") # Maximises window (u can di this with selenium too but this is chroe options)
chrome_options.add_argument("headless")   #This will not open brower but will help perform all action quicker
chrome_options.add_argument("--ignore-certificate-errors") #if there are any SSL etc certificate ehich you have to accept b4 reaching site
                                                            #programcreek.com/selenium webdriver chrome options for more browser options


driver = webdriver.Chrome(executable_path="/Users/shivanigambhir/Downloads/chromedriver 8.51.34 PM", options=chrome_options) #make connections with above

driver.get("https://www.rahulshettyacademy.com/angularpractice/")

print (driver.title)  # To print tittle of page