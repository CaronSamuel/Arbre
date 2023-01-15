import json

with open('entier.json', encoding='utf-8') as json_file:
    data : dict = json.load(json_file)

def check(data, mustHaveKeys):
    for key in mustHaveKeys:
        if(key not in data[0]):
            return False
    return True
            
    
if __name__ == "__main__":
    
    print(check(data, ['prenom', 'python']), "\t / should be FALSE")
    print(check(data, ['prenom', 'nom']), "\t / should be TRUE")
    print(check(data, ['prenom']), "\t / should be TRUE")
    print(check(data, ['patronyme']), "\t / should be FALSE")
    print(check(data, []), "\t / should be TRUE")