#Q2.Write a program to convert python objects to json data.

import json

dict={'name':'David','class':'1','age':6}
a=json.dumps(dict)
with open('meraki2','w') as dict1:
    json.dump(dict,dict1,indent=2)
