#Aapko 4 dictionaries create karni hai jaise ki emp1 emp2 emp3 and emp4.
#har ek employee ka dictionary main name,designation,age and salary honi chahiye.
#aur ye sab dictionary ki keys hai jismai maine list main value di hai.
#Iska use kar ke aapko ek json file create karni hai? 

import json

a=['Neelam','programer',24,2400]
b=['Komal','trainer',24,20000]
c=['Anuradha','HR',25,40000]
d=['Abhishek','manager',29,63000]
e=[a,b,c,d]
list=['name','designation','age','salary']
f=['emp1','emp2','emp3','emp4']
x={}
i=0
while i<len(e):
    j=0
    s={}
    while j<len(e[i]):
        s[list[j]]=e[i][j]
        j+=1
    x[f[i]]=s
    i+=1
# print(x)
with open("meraki8.json","w") as dict:
    json.dump(x,dict,indent=4)