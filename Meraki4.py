#Q4.Write a program to convert python dictionary(sort by key) to json data.

import json

a={'4': 5,'6': 7,'1': 3,'2': 4}
b=sorted(a.values())
dict={}
for i in b:
    for k in a.keys():
        if a[k]==i:
            dict[k]=a[k]
a=open("meraki4.json","w")
json.dump(dict,a,indent=2)
