from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless")
# chrome_options.headless = True # also works

from time import sleep
import schedule

def bater_ponto(user,password):
    driver=Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get('https://www.dimepkairos.com.br/Dimep/Account/Marcacao')
    driver.find_element(By.ID,'UserName').send_keys(user)
    driver.find_element(By.ID,'Password').send_keys(password+Keys.RETURN)
    driver.quit()

class Scheduler:
    def __init__(self,user,password):
        for horario in {'09:00', '12:00', '13:00', '18:00'}:
            schedule.every().monday.at(horario).do(bater_ponto(user,password))
            schedule.every().tuesday.at(horario).do(bater_ponto(user,password))
            schedule.every().wednesday.at(horario).do(bater_ponto(user,password))
            schedule.every().thursday.at(horario).do(bater_ponto(user,password))
            schedule.every().friday.at(horario).do(bater_ponto(user,password))
        while True:
            schedule.run_pending()