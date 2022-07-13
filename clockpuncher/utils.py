from datetime import datetime

def translate(word):
    dict={
        # weekdays
        'Mon':'segunda-feira',
        'Tue':'terça-feira',
        'Wed':'quarta-feira',
        'Thu':'quinta-feira',
        'Fri':'sexta-feira',

        # months
        'Jan':'janeiro',
        'Feb':'fevereiro',
        'Mar':'março',
        'Apr':'abril',
        'May':'maio',
        'Jun':'junho',
        'Jul':'julho',
        'Aug':'agosto',
        'Sep':'setembro',
        'Oct':'outubro',
        'Nov':'novembro',
        'Dec':'dezembro'
    }
    return dict[word] 

def datetime_logger(function):

    def wrapper(*args,**kwargs):
        print(f'Function: {function.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        return function(*args,**kwargs)

    return wrapper