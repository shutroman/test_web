import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://localhost:5000/login")

time.sleep(2)
def data_input():
    email = driver.find_element_by_name('email') # login
    email.send_keys('ivanivanovich1234@mail.ru')
    password = driver.find_element_by_name('password')
    password.send_keys('12345asdf')
    remember_me = driver.find_element_by_css_selector('label > input') # проверем, работает ли функция запомнить пользователя
    remember_me.click()
    sing_up = driver.find_element_by_css_selector('button')
    sing_up.click()
data_input()