import json
from exercice2 import printListRecord
from typing import Callable as cb

with open('entier.json', encoding='utf-8') as json_file:
    data : dict = json.load(json_file)
    
def firstUp(rec, key):
    data2 = dict(rec)
    data2[key] = data2[key].capitalize()
    return data2

def formatValue(rec, key, formatfunction : cb[[dict, str], dict]):
    return formatfunction(rec, key)
    
def formatRecordList(recs, key, formatfunction : cb[[dict, str], dict]):
    return formatfunction(recs, key)

if __name__ == '__main__':
    print(firstUp(data[0], 'nom'))
    print('-------------------------------------')
    print(formatValue(data[0], 'nom', firstUp))