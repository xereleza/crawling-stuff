from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from schedule import Scheduler
from utils import translate, datetime_logger
from time import sleep

class ClockPuncher:
    
    routine=('09:00', '12:00', '13:11', '18:00')

    chrome_options = Options()
    chrome_options.add_argument("--headless")

    chrome_service = Service(ChromeDriverManager().install())

    def __init__(self,user,password):
        self.user = user
        self.password = password

        self.main_scheduler = Scheduler()
        self.schedule_my_week()

        self.monitor = Scheduler()
        self.monitor.every().hour.do(self.notify_next_run)
        
        self.notify_next_run()

    def notify_next_run(self):
        try:
            weekday,month,day,time,year = min([job.next_run for job in self.main_scheduler.get_jobs()]).ctime().split(' ')
        except ValueError:
            weekday,month,trash,day,time,year = min([job.next_run for job in self.main_scheduler.get_jobs()]).ctime().split(' ')
        print(f'\npróxima execução: {translate(weekday)}, dia {day} de {translate(month)} de {year}, às {time[:-3]}')

    def schedule_my_week(self):
        print(f'\nagendando rotina para o usuário "{self.user}"...')
        for time in self.routine:
            self.main_scheduler.every().monday.at(time).do(self.clock_in)
            self.main_scheduler.every().tuesday.at(time).do(self.clock_in)
            self.main_scheduler.every().wednesday.at(time).do(self.clock_in)
            self.main_scheduler.every().thursday.at(time).do(self.clock_in)
            self.main_scheduler.every().friday.at(time).do(self.clock_in)
        print('\nhorários agendados semanalmente: {}'.format(', '.join([x for x in self.routine])))
        
    def run(self):
        while True:
            self.main_scheduler.run_pending()
            self.monitor.run_pending()
            sleep(1)
    
    @datetime_logger
    def clock_in(self):
        driver = Chrome(service = self.chrome_service, options = self.chrome_options)
        driver.implicitly_wait(10)
        driver.get('https://www.dimepkairos.com.br/Dimep/Account/Marcacao')
        driver.find_element(By.ID,'UserName').send_keys(self.user)
        driver.find_element(By.ID,'Password').send_keys(self.password+Keys.RETURN)
        driver.quit()