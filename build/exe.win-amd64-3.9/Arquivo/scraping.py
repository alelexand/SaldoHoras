import getpass
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import os
import shutil
import datetime

pyautogui.PAUSE = 0.5


class Romeu:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.user = getpass.getuser()
        self.url = "https://app.tangerino.com.br/"
        self.source = rf"C:\Users\{self.user}\Downloads/"
        self.destination = fr"T:\DEPARTAMENTOS\AUTOMAÇÃO\PROJETOS\Robo_saldo_de_horas/"
        self.datafp = datetime.date.today()
        self.datafa = datetime.date.today()
        mesantes = self.datafp.replace(day=1)
        anteriorM = mesantes - datetime.timedelta(days=1)
        self.datainicio = anteriorM.replace(day=10)
        self.datainicio = datetime.date.strftime(self.datainicio, '%d%m%Y')
        self.datafa = self.datafa.replace(day=9)
        self.datafa = datetime.date.strftime(self.datafa, '%d%m%Y')

        if os.path.exists(fr"{self.destination}/RelatorioBancoHoras.xlsx"):
            os.remove(fr"{self.destination}/RelatorioBancoHoras.xlsx")
        else:
            pass
        if os.path.exists(fr"{self.destination}/RelatorioBancoHoras.xls"):
            os.remove(fr"{self.destination}/RelatorioBancoHoras.xls")
        else:
            pass

    def acessando(self):
        self.driver.get(self.url)
        # buscando site

    def login(self):
        self.driver.maximize_window()
        time.sleep(8)
        # parte login, botão colaborador
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/form/fieldset/ul/li[2]/a').click()
        time.sleep(3)
        # parte login, usuário
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[2]/div/div[2]/div/dl/dd/fieldset/form/div[2]/input').send_keys(
            'TILIJ')
        time.sleep(1)
        # parte login, senha
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[2]/div/div[2]/div/dl/dd/fieldset/form/div[3]/input').send_keys(
            '2956')
        time.sleep(1)
        # parte login, entrar
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[2]/div/div[2]/div/dl/dd/fieldset/form/div[5]/input').click()
        time.sleep(5)

    def dentro(self):
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/span/nav[2]/ul/li[4]/div').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/span/nav[2]/ul/li[4]/dl/dd[2]/a/span').click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/span/div/div[2]/form/fieldset/div['
                                           '8]/input').click()
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('del')
        pyautogui.press('backspace')
        pyautogui.press('del')
        pyautogui.press('backspace')
        pyautogui.press('del')
        pyautogui.press('backspace')
        pyautogui.press('del')
        pyautogui.press('backspace')
        pyautogui.press('del')
        pyautogui.press('backspace')
        pyautogui.press('del')
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.write(f'{self.datainicio}')
        pyautogui.press('tab')
        pyautogui.press('del')
        pyautogui.press('backspace')
        pyautogui.press('del')
        pyautogui.press('backspace')
        pyautogui.press('del')
        pyautogui.press('backspace')
        pyautogui.press('del')
        pyautogui.press('backspace')
        pyautogui.press('del')
        pyautogui.press('backspace')
        pyautogui.press('del')
        pyautogui.press('backspace')
        pyautogui.press('backspace')
        pyautogui.write(f'{self.datafa}')
        pyautogui.press('tab')
        pyautogui.press('enter')
        pyautogui.press('up')
        pyautogui.press('enter')
        pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(40)
        files = os.listdir(self.source)
        # mudança de armazenamento da planilha
        for file in files:
            if file.find(".xls") >= 0:
                shutil.move(rf"{self.source}/RelatorioBancoHoras.xls", self.destination)
                break
        time.sleep(2)
        self.driver.close()


