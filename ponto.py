from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless")

import schedule

def crawl(user,password):
    driver=Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.get('https://www.dimepkairos.com.br/Dimep/Account/Marcacao')
    driver.find_element(By.ID,'UserName').send_keys(user)
    driver.find_element(By.ID,'Password').send_keys(password+Keys.RETURN)
    driver.quit()

class Scheduler:
    def __init__(self,user,password):
        self.user=user
        self.password=password
        for horario in {'09:00', '12:00', '13:00', '18:00'}:
            schedule.every().monday.at(horario).do(self.bater_ponto)
            schedule.every().tuesday.at(horario).do(self.bater_ponto)
            schedule.every().wednesday.at(horario).do(self.bater_ponto)
            schedule.every().thursday.at(horario).do(self.bater_ponto)
            schedule.every().friday.at(horario).do(self.bater_ponto)
        while True:
            schedule.run_pending()
    
    def bater_ponto(self):
        crawl(self.user,self.password)
