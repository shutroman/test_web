import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://localhost:5000/signup")

time.sleep(2)
def data_input():
    email = driver.find_element_by_name('email') # registration
    email.send_keys('ivanivanovich12345@mail.ru')
    password = driver.find_element_by_name('password')
    password.send_keys('12345asdf')
    sing_up = driver.find_element_by_css_selector('button')
    sing_up.click()
data_input()
time.sleep(2)
data_input() # login
