from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import schedule
from datetime import datetime

chrome_options = Options()
#chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless")

class Scheduler:

    def __init__(self,user,password):
        self.user=user
        self.password=password
        self.schedule()

    def schedule(self):
        rotina=('09:00', '12:00', '13:00', '18:00')
        #scheduled=''
        for horario in rotina:
            schedule.every().monday.at(horario).do(self.bater_ponto)
            schedule.every().tuesday.at(horario).do(self.bater_ponto)
            schedule.every().wednesday.at(horario).do(self.bater_ponto)
            schedule.every().thursday.at(horario).do(self.bater_ponto)
            schedule.every().friday.at(horario).do(self.bater_ponto)
        scheduled=', '.join([x for x in rotina])
        print(f'horários agendados: {scheduled}')
        #print(schedule.get_jobs())

    def run(self):
        while True:
            schedule.run_pending()
    
    def bater_ponto(self):
        driver=Chrome(options=chrome_options)
        driver.implicitly_wait(10)
        driver.get('https://www.dimepkairos.com.br/Dimep/Account/Marcacao')
        driver.find_element(By.ID,'UserName').send_keys(self.user)
        driver.find_element(By.ID,'Password').send_keys(self.password+Keys.RETURN)
        datetime_isostring=datetime.now().replace(microsecond=0).isoformat()
        date,time=datetime_isostring.split('T')
        print(f'marcação de ponto realizada no dia {date} às {time}')
        driver.quit()
