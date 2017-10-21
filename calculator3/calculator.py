#!/usr/bin/env python3
import sys
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
        return float(self._config[config_option])

class UserData(object):
    def __init__(self,userdatafile):
        self._userdata={}
        self._filename=userdatafile
        with open(self._filename) as file:
            for line in file:
                line=line.strip() 
                line=line.split(',')
                self._userdata[line[0]]=line[1]
 
    def calculator(self):
        ins=Config('test.cfg')
        insurance_rate=ins.get_config('YangLao')+ins.get_config('YiLiao')+ins.get_config('ShiYe')+ins.get_config('GongShang')+ins.get_config('ShengYu')+ins.get_config('GongJiJin')
        tlist=[(3/100,0),(10/100,105),(20/100,555),(25/100,1005),(30/100,2755),(35/100,5505),(45/100,13505)]
        for n,s in self._userdata.items():
            s=float(s)
            low=ins.get_config('JiShuL')
            high=ins.get_config('JiShuH')
            if(s<low):
                insurance=low*insurance_rate
            if(s>high):
                insurance=high*insurance_rate
            else:
                insurance=s*insurance_rate
            # calculate taxable income
            tax_in=s-insurance-3500 
            # judge and calculate final tax
            if(tax_in<=1500 and tax_in>0):
                tax=tax_in*tlist[0][0]-tlist[0][1]
            elif(tax_in<=4500 and tax_in>1500):
                tax=tax_in*tlist[1][0]-tlist[1][1]
            elif(tax_in<=9000 and tax_in>4500):
                tax=tax_in*tlist[2][0]-tlist[2][1]
            elif(tax_in<=35000 and tax_in>9000):
                tax=tax_in*tlist[3][0]-tlist[3][1]
            elif(tax_in<=55000 and tax_in>35000):
                tax=tax_in*tlist[4][0]-tlist[4][1]
            elif(tax_in<=80000 and tax_in>55000):
                tax=tax_in*tlist[5][0]-tlist[5][1]
            elif(tax_in>80000):
                tax=tax_in*tlist[6][0]-tlist[6][1]
            else:
                tax=0
            salary=s-tax-insurance
            single=[format(s,".0f"),format(insurance,".2f"),format(tax,".2f"),format(salary,".2f")]
            self._userdata[n]=single
        return self._userdata
       # print(self._userdata)
    def dumptofile(self,outputfile):
        d=self.calculator()
        with open(outputfile,'w') as f:
            for k,v in d.items():
                line=k+','+v[0]+','+v[1]+','+v[2]+','+v[3]+'\n'
               # print(line)
                f.write(line)
try:
    args=sys.argv[1:]
    index=args.index('-c')
    configfile=args[index+1]
    index=args.index('-d')
    userfile=args[index+1]
    index=args.index('-o')
    printfile=args[index+1]
except:
    exit(0)
staff=UserData(userfile)
staff.dumptofile(printfile)
       
