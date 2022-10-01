from lib2to3.pgen2 import driver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://vk.com/feed")
print("Application title is",driver.title)
print("Application url is",driver.current_url)
driver.quit()