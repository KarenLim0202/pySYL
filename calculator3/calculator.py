class Config(object):
    def __init__(self,configfile):
        self._config={}
        self._filename=configfile
        with open(self._filename) as file:
            for line in file:
                line=line.strip()
                line=line.split('=')
                self._config[line[0].strip()]=line[1].strip()
    def get_config(self,config_option):
        print(self._config)
        return self._config[config_option]

class UserData(object):
    def __init__(self,userdatafile):
        self._userdata={}
        self._filename=userdatafile
        with open(self._filename) as file:
            for line in file:
                line=line.strip() 
                line=line.split(':')
                self._userdata[line[0]]=line[1]
            print(self._userdata)

insurance=Config('test.cfg')
print(insurance.get_config('JiShuL')) 
staff=UserData('user.csv') 
print(sta)       
