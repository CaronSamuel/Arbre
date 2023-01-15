import json
from exercice2 import printListRecord

with open('entier.json', encoding='utf-8') as json_file:
    data : dict = json.load(json_file)
    
def keepKeys(rec, keys):
    list_all_keys = []
    for key in data[0]:
        list_all_keys.append(key)
    #print(list_all_keys)
    for j in range (0, len(keys)):
        list_all_keys.remove(keys[j])
        j = j + 1
    #print(list_all_keys)
    data2 = dict(rec)
    for i in range(0, len(list_all_keys)):
        del data2[list_all_keys[i]]
    return data2
    
    
def keepKeysInList(rec, keys):
    list_all_keys = []
    for key in data[0]:
        list_all_keys.append(key)
    #print(list_all_keys)
    for j in range (0, len(keys)):
        list_all_keys.remove(keys[j])
        j = j + 1
    #print(list_all_keys)
    data2 = list(rec)
    for k in range (0, len(data2)):
        for i in range (0, len(list_all_keys)):
            del data2[k][list_all_keys[i]]
    return data2



if __name__ == '__main__':
    print(keepKeys(data[0], ['age', 'prenom']))
    print('-------------------------------------')
    printListRecord(keepKeysInList(data, ['age' , 'nom']))
    