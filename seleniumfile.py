from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pytest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome("C:\webdrivers\chromedriver_win32\chromedriver.exe")
driver.get(aseemsri-trials7401.orangehrmlive.com")
driver.maximize_window()
search=driver.find_element_by_name("txtUsername")
search.send_keys("Admin")
password=driver.find_element_by_name("txtPassword")
password.send_keys(" IsBQ1m1@Lv")
search.send_keys(Keys.RETURN)
y=driver.title

driver.find_element_by_xpath("//*[@id='account-job']/i").click()
time.sleep(5)
driver.find_element_by_xpath("//a[text()='About']").click()
time.sleep(10)

try:
    ele=WebDriverWait(driver,20).until(
        EC.presence_of_element_located((By.XPATH,"//*[@id='companyInfo']/div/div[1]/p"))
    )
except:
    driver.quit()

text = driver.find_element_by_xpath("//*[@id='companyInfo']/div/div[1]/p").text
time.sleep(5)
driver.find_element_by_xpath("//*[@id='heartbeatCancelBtn']").click()

time.sleep(5)

try:
    ele1=WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,"//*[@id='menu_pim_viewPimModule']/a/span[2]"))
    )
except:
    driver.quit()

driver.find_element_by_xpath("//*[@id='menu_pim_viewPimModule']/a/span[2]").click()

time.sleep(5)
driver.find_element_by_xpath("//*[@id='menu_pim_addEmployee']/span[2]").click()
time.sleep(5)
driver.implicitly_wait(100)

try:
    ele2=WebDriverWait(driver,20).until(
        EC.presence_of_element_located((By.ID,"first-name-box"))
    )
except:
    driver.quit()

driver.implicitly_wait(20)

firstname=driver.find_element_by_id("first-name-box")
firstname.send_keys("Shyam")
time.sleep(2)

driver.find_element_by_id("middle-name-box").send_keys("bahadur")
time.sleep(2)
driver.find_element_by_id("last-name-box").send_keys("singh")
time.sleep(2)


driver.find_element(By.XPATH,"//*[@id='modal-holder']/div/div/div/div[2]/form/oxd-decorator/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/button/i[2]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='bs-select-1-7']").click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="modal-save-button"]').click()
time.sleep(3)
driver.implicitly_wait(50)

try:
    driver.find_element_by_xpath('//*[@id="wizard-nav-button-section"]/button[2]').click()

except:
    print("not able to proceed")


driver.find_element_by_xpath('//*[@id="menu_pim_viewEmployeeList"]/span[2]').click()
time.sleep(3)
driver.implicitly_wait(10)
t=driver.find_element_by_xpath('//*[@id="employee_name_quick_filter_employee_list_value"]')
t.send_keys('ram')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="quick_search_icon"]').click()
time.sleep(5)

driver.find_element_by_xpath('//*[@id="employeeListTable"]/tbody/tr/td[3]').click()
driver.implicitly_wait(10)
time.sleep(5)



time.sleep(10)
driver.implicitly_wait(20)
driver.quit()



def test_dashboard():
    assert y=='Dashboard'
def test_text():
    assert text=="Company Name: OrangeHRM (Pvt) Ltd(Parallel Demo)"

