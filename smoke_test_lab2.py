import time
from enum import Enum
from lib2to3.pgen2 import driver

from numpy import number
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#Устанавливаем 
webDriver = webdriver.Chrome(ChromeDriverManager().install())
#функция вставляет тип конвертации и текст для конвертации 
def test_generation(register_type,text):
    #register_type - тип конвертации
    #text - строки для конвертации
    
    #Ищет по наименованию конвертации нужный эллемент и нажимает на него
    webDriver.find_element(By.ID,"method-tabs").find_element(By.LINK_TEXT,register_type).click()
    #Проверят что нажатый эллемент соответствует передаваемому пользователем
    assert register_type == webDriver.find_element(By.ID,"method-tabs").find_element(By.CLASS_NAME,"selected").get_property("text") 
    #Отправляет текст в блок текста 
    webDriver.find_element(By.ID,"source").send_keys(text)
    time.sleep(2)
    #Проверяет что отправленный текст находится в этом блоке и соответствует тому который мы передавали
    assert text == webDriver.find_element(By.ID,"source").get_attribute("value")
    #Получаем сконвертированное слово и возвращаем из функции
    word = webDriver.find_element(By.ID,"target").get_attribute("value")
    return word

#Функция проверяет соответсвие цифры введенной пользователем с цифрой в списке и возвращает наименование категории конвертации
def choose_register_type(user_number):
    return {
        '1': "ВЕРХНИЙ РЕГИСТР",
        '2': "нижний регистр",
        '3': "Заглавные Буквы",
        '4': "иНВЕРСИЯ рЕГИСТРА",
        '5': "По предложениям"
    }[user_number]

#Получаем URL сайта 
webDriver.get("https://www.artlebedev.ru/case/")
time.sleep(2)
#Выдаем пользователю типа конвертации 
print("Выберите тип регистра(цифрой): \n" + "1.Верхний регистр \n" + "2.Нижний регистр \n" + "3.Заглавные буквы \n" + "4.Инверсия регистра \n" + "5.По предложениям")

#Просим пользователя поставить цифру и проверяем цифру на соответствие в функции choose_register_type
converter_type = choose_register_type(input("Введите цифру: ")) 
text_for_converter = input("Введите строку для конвертации: ")

#Передаем переменные converter_type и text_for_converter в функцию test_generation
converter_word = test_generation(converter_type,text_for_converter)
#Печатаем сконвертированное слово
print("Конвертированное слово: " + converter_word)
#Закрываем вкладку
webDriver.close()
