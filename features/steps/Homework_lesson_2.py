

#logo
driver.find_element(By.XPATH, '//div/a[@href="/ref=ap_frn_logo"]') .click()
driver.back()
#login
email=driver.find_element(By.ID, 'ap_email_login')
sleep(2)
email.send_keys("test@example.com")

sleep(5)
#continue
driver.find_element(By.ID, 'continue').click()
#Conditions of Use
driver.find_element(By.XPATH, "(//a[contains(text(),'Conditions of Use')])[2]").click()
#privacy
#privacy = driver.find_element(By.PARTIAL_LINK_TEXT, "Privacy ").click()
#Need help
#driver.find_element(By.CSS_SELECTOR,"a[role='button']").click()
#forget password
#driver.find_element(By.ID, 'auth-fpp-link-bottom').click()

---------------------------------------------------------------------------------------------------------------------------
#www.target.com

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
# open the url
driver.get('https://www.target.com/')
sleep(5)
driver.find_element(By.XPATH,"//span[text()='Account']").click()
sleep(5)
driver.find_element(By.XPATH,"//div/button[@data-test='accountNav-signIn']").click()
sleep(5)
print("Test Passed: Signin page opened successfully")
driver.quit()

-----------------------------------------------------------------------------------------------------------------------------
#search


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
# open the url
driver.get('https://www.target.com/')
sleep(5)
driver.find_element(By.XPATH,"//input[@data-test='@web/Search/SearchInput']").send_keys("apple watch")

driver.find_element(By.XPATH,"//button[@data-test='@web/Search/SearchButton']").click()
sleep(5)
driver.quit()