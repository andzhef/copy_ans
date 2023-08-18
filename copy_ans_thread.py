from pathlib import WindowsPath
from datetime import datetime

class AnsCopier:
    

    def __init__(self, path_to_ans_source, path_to_cons, last_update_date):
        self.path_to_ans = WindowsPath(path_to_ans_source)
        self.path_to_cons = WindowsPath(path_to_cons)
        self.path_to_base = path_to_cons/'BASE'
        self.last_date_update = time.mktime(time.strptime(date_last_update_base,'%d-%m-%y'))
        self.ans_to_copy:list = None
        
    def _form_bases_list(self):
        """Формируем список баз в комплекте по baselist"""
        path_to_baselist = self.path_to_base/'baselist.cfg'
        with open(path_to_baselist, encoding = 'utf8') as bl:
            bases: list = bl.read().strip().split('\n')
        return bases
    
    def prepare_ans(self):
        """Отбираем из списка всех файлов пополнения, с названием баз и с датой, позже дня последнего пополнения"""
        good_for_date: list = []
        for one_ans in self.path_to_ans.iterdir():
            if one_ans.stat()[8] > self.last_date_update:
                good_for_date.append(one)
        return good_for_date

    def 

    def copyer_run(self):
        prepare_ans()
        copy_ans()
        

def main():
    ANS_SOURCE = r'G:\m-style\Update'
    CONSULTANT_FOR_UPDATE = [('01.08.2023', r'C:\Veda')]
    #TEST
    
    

if __name__ == '__main__':
    main()

