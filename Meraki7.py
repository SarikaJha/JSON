#Q7.Text file data ko json file data mai convert karo,jaise ki neeche diya hai?
# Convert text file data to json file data, as given below?
#Text.txt:-  
#  Name Abhishek
#  Designation CEO of navgurukul
#  Gender male
#  Age 29

# Output:-
# Json_file.json:-
# {
#     "Name": "Abhishek",
#     "Designation": "CEO of navgurukul",
#     "Gender":"male",
#     "Age": "29"
# }

import json
a={}
filename="meraki7.file"
with open("meraki7.file") as f:
    for i in f:
        key,value=i.strip().split(None,1)
        a[key]=value
# print(json.dumps(a,indent=4))
file=open("meraki7.json","w")
json.dump(a,file,indent=4)
file.close()
