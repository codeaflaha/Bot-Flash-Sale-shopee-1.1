from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(ChromeDriverManager().install())


     
driver.get("https://shopee.co.id/buyer/login?from=https%3A%2F%2Fshopee.co.id%2Fproduct-i.241308147.7153405500%3Fsmtt%3D0.218879583-1605157013.9&next=https%3A%2F%2Fshopee.co.id%2Fproduct-i.241308147.7153405500%3Fsmtt%3D0.218879583-1605157013.9&smtt=0.218879583-1605157013.9") #this is the link above
#username = driver.find_element_by_id("Username")
#password = driver.find_element_by_id("Password")
username = "username@gmail.com"
password = "password"

AkunID = driver.find_element_by_class_name('_56AraZ')
AkunID.send_keys(username)

AkunID.send_keys(Keys.TAB,password,Keys.ENTER)


