from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()

try:
    #1. Перейти по ссылке на главную страницу сайта Netpeak (https://netpeak.ua/)
    browser.get(url='https://netpeak.ua/')
    time.sleep(1)

    #2. Нажать на кнопку "О нас" и в выпавшем списке нажать кнопку "Команда"
    button_aboutUs = browser.find_elements(By.CLASS_NAME, 'main-link')[2]
    button_aboutUs.click()
    time.sleep(1)
    browser.find_element(By.PARTIAL_LINK_TEXT, 'Команда').click()

    #3. Нажать кнопку "Стать частью команды"
    # и убедится что в новой вкладке открылась страница Работа в Нетпик
    browser.find_element(By.PARTIAL_LINK_TEXT, 'Стать частью команды').click()
    browser.switch_to.window(browser.window_handles[1])
    print("3.Tab title:", browser.title)
    time.sleep(1)

    #4. Убедится что на странице есть кнопка "Я хочу работать в Netpeak"
    # и на нее можно кликнуть
    button = browser.find_element(By.PARTIAL_LINK_TEXT, 'Я хочу работать в Netpeak')
    href_data = button.get_attribute('href')
    print('4.Is the button active:', href_data is not None)
    time.sleep(1)

    #5. Вернутся на предыдущую вкладку и нажать кнопку "Личный кабинет"
    browser.close()
    browser.switch_to.window(browser.window_handles[0])
    browser.find_element(By.PARTIAL_LINK_TEXT, 'Личный кабинет').click()
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(1)

    #6. На странице личного кабинета заполнить Логин и Пароль
    # случайными данными.
    email_input = browser.find_element(By.ID, 'login')
    email_input.clear()
    email_input.send_keys('0933417361')

    password_input = browser.find_element(By.ID, 'password')
    password_input.clear()
    password_input.send_keys('dskfjsldf')
    time.sleep(1)

    #7. Проверить что кнопка "Войти" не доступна
    button_log = browser.find_element(By.XPATH, '//button[@class="enter md-button md-ink-ripple"]')
    print('7.The button is not active?', button_log.get_attribute("disabled"))

    #8. Отметить чекбокс "Авторизируясь, вы соглашаетесь с Политикой конфиденциальности"
    privacy_policy = browser.find_elements(By.XPATH, '//div[@class="md-container"]')[1]
    privacy_policy.click()

    #9. Нажать на кнопку войти и проверить наличие нотификации о неправильном логине или пароле
    button_log.click()
    time.sleep(1)
    notification = browser.find_element(By.CLASS_NAME, 'md-toast-content')
    notif = notification.get_attribute('class')
    print('9.Execution notification:', notif is not None)

    #10. Проверить что Логин и Пароль подсветились красным цветом
    rgb_email = browser.find_element(By.ID, 'login').value_of_css_property('border-color')
    rgb_password = browser.find_element(By.ID, 'password').value_of_css_property('border-color')
    browser.save_screenshot('10_color_log.png')
    print('10.Color email and password:', rgb_email, rgb_password)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()
