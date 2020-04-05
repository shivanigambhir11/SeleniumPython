from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/shivanigambhir/Downloads/chromedriver 8.51.34 PM")
driver.get("https://www.rahulshettyacademy.com/angularpractice/")

driver.find_element_by_link_text("Shop").click()
driver.find_elements_by_xpath("//div[@class = 'card h-100']")
# print (driver.find_elements_by_xpath("//h4[@class ='card-title']").text)
Products=driver.find_elements_by_xpath("//h4[@class ='card-title']")

for product in Products:
    print (product.text)
    if product == 'Blackberry':
        product.find_elements_by_xpath("//div[@class = 'card h-100']/div/button").click()

#driver.find_element_by_xpath("//a[@class= 'nav-link btn btn-primary']").click()




