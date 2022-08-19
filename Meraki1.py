#Q1.Write a program to convert json data into python objects.

import json

x='{"name":"John","age":30,"city":"New York"}'
y=json.loads(x)
print(y)
