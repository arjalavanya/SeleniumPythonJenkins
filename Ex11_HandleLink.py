import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
class MyTestCase(unittest.TestCase):
    def test01(self):
        filePath = "C:\\Users\\LAARJA\\PycharmProjects\\SeleniumPythonProject\\drivers\\chromedriver.exe"
        url = "https://parabank.parasoft.com/parabank/index.htm"
        driver = webdriver.Chrome(filePath)
        time.sleep(1)
        driver.get(url)
        time.sleep(1)
        linkList = driver.find_elements(By.TAG_NAME, "a")
        linkCount = len(linkList)
        print("Total no. of links:" , linkCount)
        time.sleep(1)
        driver.quit()
if __name__ == '__main__':
    unittest.main()