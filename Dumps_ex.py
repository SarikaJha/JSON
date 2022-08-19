import json

x={1:'John','age':30,'city':'New York'}
y=json.dumps(x)
print(y)

# # y=json.dumps(x,indent=2)
# # print(y)

# y=json.dumps(x,indent=2,separators=(" ","="))
# print(y)