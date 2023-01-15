import json

with open('entier.json', encoding='utf-8') as json_file:
    data : dict = json.load(json_file)
    
# Question 1
def delKey(rec, key):
    data2 = dict(rec)
    del data2[key]
    return data2

# Question 2
def delKeys(rec, keys):
    data2 = dict(rec)
    for key in keys:
        del data2[key]
    return data2

# Question 3
def delKeysInList(rec, keys):
    data2 = list(rec)
    for key in keys:
        for i in range (0, len(data2)):
            del data2[i][key]
    return data2
    
    
# Question 5
def printListRecord(listOfDict):
    for item in listOfDict:
        print(item)

if __name__ == '__main__':
    print(delKey(data[0], 'nom'))
    print(delKeys(data[0], ['nom', 'age']))
    print('----------------------------')
    print(printListRecord(data))
    print('----------------------------')
    printListRecord(delKeysInList(data, ['nom', 'prenom']))