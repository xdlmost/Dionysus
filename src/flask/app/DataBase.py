
class DictFileDataBase:
    def __init__(self):
        pass
class DataBase:
    def __init__(self ,dataBaseType='dict_file'):
        if dataBaseType == 'dict_file':
            self.__interDataBase =DictFileDataBase()
