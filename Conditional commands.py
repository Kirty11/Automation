from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()

driver.get("https://github.com/login")
print(driver.title)  #Title of the page

user_ele=driver.find_element_by_name("login")
print(user_ele.is_displayed())#True or False based on element's status
print(user_ele.is_enabled())

pwd_ele=driver.find_element_by_name("password")
print(pwd_ele.is_displayed())#True or False based on element's status
print(pwd_ele.is_enabled())

user_ele.send_keys("skirty066@gmail.com")
pwd_ele.send_keys("Kirty@123")

driver.find_element_by_name("commit").click()
#driver.close()

