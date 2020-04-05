
from selenium import webdriver

#browser exposes executable file


#invoking exe file to invoke browser

driver = webdriver.Chrome(executable_path="/Users/shivanigambhir/Downloads/chromedriver 8.51.34 PM")


#driver=webdriver.Firefox(executable_path="/Users/shivanigambhir/Downloads/geckodriver 4")

# get execuatble path ofIE and try forr that

driver.get("https://www.rahulshettyacademy.com/")


print (driver.title)

print (driver.current_url)

driver.get('https://www.rahulshettyacademy.com/#/mentorship')
driver.maximize_window()
driver.minimize_window()
driver.back()
driver.refresh()


driver.close()