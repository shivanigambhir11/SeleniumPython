from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path="/Users/shivanigambhir/Downloads/chromedriver 8.51.34 PM")
driver.implicitly_wait(5)   # giving time for promo cpde to get applied
driver.get("https://www.rahulshettyacademy.com/seleniumPractise/")

driver.find_element_by_css_selector("input[class='search-keyword']").send_keys("ber")  #putting "ber" in search box
time.sleep(4)     #giving time to find
driver.find_element_by_css_selector("input.search-keyword").click() # click on search icon
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))   # couynt list of items after seaching
assert count == 3    # check if count is same to what you counted

list= []
buttons = driver.find_elements_by_xpath("//div[@class = 'product-action']/button")   # click on add to cart of all 3 items using loop
for button in buttons:                                                               #get value of all products
    list.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)     # in loop we are adding product text in list too
    button.click()                                                                   #clicking on add to cart
print (list)

driver.find_element_by_css_selector("img[alt='Cart']").click()                      #click on cart to check number of items
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()      #click on proceed to checkout

list2= []
veggies = driver.find_elements_by_css_selector("p.product-name")                    #find product name on page 2 to map
for veg in veggies:
    list2.append(veg.text)
print(list2)

originalAmount = driver.find_element_by_class_name("discountAmt").text               # check original amout before doscount
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")       # type promocode
driver.find_element_by_class_name("promoBtn").click()                                # apply code
discountedAmount = driver.find_element_by_class_name("discountAmt").text

#assert float(discountedAmount) < int (originalAmount)

print (driver.find_element_by_class_name("promoInfo").text)                          # validate text
#assert list == list2

amounts = driver.find_elements_by_xpath("//tr/td[5]/p")                              # find amount of fruits

sum = 0
for amount in amounts:                                                               # Loop for adding finding and adding money one by one
    int(amount.text)
    sum = sum + int (amount.text)
print (sum)

TotalAmount = int(driver.find_element_by_class_name("totAmt").text)

assert TotalAmount == sum














