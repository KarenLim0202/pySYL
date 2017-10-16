#!/usr/bin/env python3
import sys
try:
    income= int(sys.argv[1])
except:
    print("Parameter Error")

tlist=[(3/100,0),(10/100,105),(20/100,555),(25/100,1005),(30/100,2755),(35/100,5505),(45/100,13505)]
# calculate taxable income
tax_in=income-3500 
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

print(format(tax,".2f"))
    


