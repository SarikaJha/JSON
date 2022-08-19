#Apki dictionary ka use kar ke ek json file create karna hai.
# Aur apko kuch task perform karne hai jaise ki
# 1.main dekhna chahta hu shopping list ko json file dekhna.
# 2.phir main user se poochu ga ki kon sa item khareedna chahte ho.
# 3.uske baad user name dega phir user se input poochege jaise ki tum kitne item chahte ho.
# 4.phir aapka wo number of items json file se remove karna hai.
# 5.Agar tumhe shopping items add karna hai to tumko json file main insert karna hoga.

import json

a={'shopping_list':{'chaco':15,'biscuit':50,'diary_milk':30,'ice-cream':20}}
x=input("enter the item:")
y=int(input("enter the number you want:"))
dict={}
dict1={}
for i in a:
    if a[i]==a[i]:
        b=a[i][x]
        s=int(b)
        n=s-y
for j in a[i]:
    dict[j]=a[i][j]
    if j==x:
        dict[j]=n
        dict1[i]=dict
print(dict1)
f=open("meraki9.json","w")
json.dump(dict1,f,indent=4)
f.close() 