import json

with open('entier.json', encoding='utf-8') as json_file:
    data : dict = json.load(json_file)
    
# print(data, 'type', type(data))

print("Les clés sont : ")
for cle in data[0]:
    print(cle)
    
print()

print("Les valeurs sont : ")
for value in data:
    print(value.values())
    
print()

print("Les items sont : ")
for item in data:
    print(item) 
    
print() 
    
print("Monsieur Cozot a désormais 15 ans : ")
data[0]['age'] = 15

print(data[0])