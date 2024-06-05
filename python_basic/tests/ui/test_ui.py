import pytest
#import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
#метод пошуку елементів за певними атрибутами
from selenium.webdriver.common.by import By

@pytest.mark.ui
def test_check_incorrect_username():
    #Створення об'єкту для керування браузером
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    """
    якщо стара версія браузеру
        driver = webdriver.Chrome(
        service=Service(r"C:\\cygwin64\\home\\inka\\QA\\" + "chromedriver.exe"))
    get - операція відкриття стрінки в браузері
    driver.get("URL")
    """
    #відкриваємо сторінку
    driver.get("https://github.com/login")
    
    #Знаходимо поле в яке будемо вводити неправильне імя користувача/емеіл
    #login_field - імя поля куди вводимо логін (подивитись в браузері через f12)
    #driver.find_element - пошук елемента за імене його атрибута та його значенням
    #driver.find_element(імя_атрибута, знач_атрибута)
    login_elem = driver.find_element(By.ID, "login_field")

    #вводимо неправильне імя користувача/пошту
    #send_keys - операція введення тексту до елемента сторінки
    #element.send_keys(текст_що_треба_ввести)
    login_elem.send_keys("mistake@gmail.com")
    #додаємо паузу, щоб побачити що все відбув правильно
    #Знаходимо поле із паролем
    pass_elem = driver.find_element(By.ID, "password")
    #вводимо нерпавильний пароль
    pass_elem.send_keys("wrong password")
    #знаходио кнопку 
    btn_elem = driver.find_element(By.NAME, "commit")
    #емулюємо клік лівою кнопкою миші 
    btn_elem.click()

    #Перевіряємо що назва сторінки така як ми очікуємо
    #title - зберігає в собі заголовок сторінки
    assert driver.title == "Sign in to GitHub · GitHub"
#    time.sleep(3)
    #закриваємо браузер
    driver.close()