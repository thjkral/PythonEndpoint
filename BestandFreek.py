# hierin functies maken die je op een bepaalde endpoint wilt laten zien. (deze functie wordt via app.py file geupdate)
import pandas as pd
import json

# Deze functie zal een product opzoeken en alle waardes die daarbij horen printen.

def prod_lookup(prod_name):

    data = pd.read_json("NutrientDatasetWithBarcodes.json", 'r')

    df = pd.DataFrame(data)

    testdf = df.copy()

    prod_name = prod_name.lower()

    prod_name = prod_name.split()

    prodList = []

    for i, product in testdf.iterrows():
        if len(prod_name) == 1:
            if prod_name[0] in product["Descrip"]:
                prodList.append(product)
        elif len(prod_name) == 2:
            if prod_name[0] in product["Descrip"] and prod_name[1] in product["Descrip"]:
                prodList.append(product)
        elif len(prod_name) == 3:
            if prod_name[0] in product["Descrip"] and prod_name[1] in product["Descrip"] and prod_name[2] in product["Descrip"]:
                prodList.append(product)
        elif len(prod_name) == 4:
            if prod_name[0] in product["Descrip"] and prod_name[1] in product["Descrip"] and prod_name[2] in product["Descrip"] and prod_name[3] in product["Descrip"]:
                prodList.append(product)
        else:
            return "Sorry nothing found"
    
    return prodList
     

# prod_lookup("chili beans")

# De functie hieronder zoek een product op aan de hand van de barcode en geeft alle values terug die aan dat product gekoppeld zijn.

def bcode_lookup(barcode):

    data = pd.read_json("NutrientDatasetWithBarcodes.json", 'r')

    df = pd.DataFrame(data)
    
    testdf = df.copy()

    for i, product in testdf.iterrows():
        if product["Barcode"] == barcode:
            return str(product)
        else:
            return "Sorry nothing found"


# bcode_lookup(2056)

# Hieronder een functie voor het opzoeken van values van een product aan de hand van de ID code.

def id_lookup(ID):

    data = pd.read_json("NutrientDatasetWithBarcodes.json", 'r')

    df = pd.DataFrame(data)
    
    testdf = df.copy()

    for i, product in testdf.iterrows():
        if product["ID"] == ID:
            return (str(product))
        else:
            return "Sorry nothing found"

# id_lookup(1019)

# Deze functie zal een barcode vervangen voor een barcode die ingegeven is als argument.
# DEZE HOEFT NIET ONLINE TE KOMEN MAAR ALLEEN TE GEBRUIKEN VOOR HET VERVANGEN VAN BARCODES VAN EEN AANTAL VOORBEELD PRODUCTEN.

# def barcode_modifier(new_barcode, prod_name):

#     data = pd.read_json("NutrientDatasetDictUpdate.json", 'r')

#     df = pd.DataFrame(data)
    
#     testdf = df.copy()

#     prod_name = prod_name.upper()

#     for i, x in testdf.iterrows():
#         if prod_name in x["ShortDescrip"]:
#             x = x.replace(x["Barcode"], new_barcode)
#             testdf.loc[i] = x
#             return (str(x))
    
# barcode_modifier(8710400044567, "TOMATO PRODUCTS,CND,PUREE,W/SALT")
# barcode_modifier(8718907108324, "CHILI WITH BEANS,CANNED")
# barcode_modifier(3083680597210, "CORN,SWT,WHITE,CKD,BLD,DRND,W/SALT")
# barcode_modifier(8000050837825, "SPAGHETTI,CKD,ENR,W/ SALT")


