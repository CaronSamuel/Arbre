import json

def loadfile(filename):
    with open(filename, encoding='utf-8') as json_file:
        data : dict = json.load(json_file)
    return data

def printallrecord(rec):
    for item in rec:
        print(item)
        
def retrieve_first(rec):
    rec.pop(0)
        
def fileEdit(rec, name):
    for i in rec:
        if (i["nom"] == name):
            print("Que voulez-vous modifier ? Le nom ? Les langages ?")
            chgt = input("Veuillez choisir -> : ")
            if (chgt == "nom"):
                print("Quelle est le nom que vous voulez rentrer ?")
                new_name = input("Veuillez donner le nom que vous voulez modifier.")
                i["nom"] = new_name
            elif (chgt == "langages"):
                print("Quels sont les langages que vous voulez donner ?")
                new_languages = input("Veuillez donner les langages que vous souhaitez modifier ou ajouter.")
                for d in "langages":
                    if (d == new_languages):
                        res = True
                        print("Que voulez modifier ? ")
                        modif_languages = input("Veuillez donner les langages que vous souhaitez modifier -> :")
                        i[d.index()] = modif_languages
                    else:
                        res = False
                        print("Que voulez ajouter ? ")
                        modif_languages = input("Veuillez donner les langages que vous souhaitez ajouter -> :")
                        i["langages"].append(new_languages)
                        
                        
def new_fiche(rec, nom : str , langages : str):
    nvl_fiche = {
        "nom" : nom,
        "langages" : langages
    }
    rec.append(nvl_fiche)
    """ x = json.dumps(nvl_fiche, indent=4)
    str = createJSONstring(x)
    print(str) """


def save_fiche(rec, fiche): 
    fiche_to_save = json.dumps(fiche, indent=4)
    json.loads(fiche_to_save)
    return rec


def save(rec):
    file = open("try.json", "w")
    file.write("[\n")
    for i in rec:
        file.write("{\n")
        file.write('"nom" : ' + '"' + i["nom"] + '"' + ",\n")
        file.write('"langages" : ' + '"' + str(i["langages"]) + '"' + "\n") 
        if(i == rec[-1]):
            file.write("}\n")
        else:
            file.write("},\n")
    file.write("\n]")
    file.close()
    
if __name__ == '__main__':
    with open("try.json", "r+") as data:
        rec = json.load(data)
        n1 = new_fiche(rec, "oui", "LAP")
        n2 = new_fiche(rec, "test", "test")
        save(rec)
        """ save_fiche(rec, n1) """
        retrieve_first(rec)
        printallrecord(rec)
                    
                    
                