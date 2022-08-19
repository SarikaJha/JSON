import json

# a={1: 3}
# mystring = json.dumps(a)
# print(mystring)


a='{"1":3}'
string=json.loads(a)
print(string)