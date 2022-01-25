# hierin functies maken die je op een bepaalde endpoint wilt laten zien. (deze functie wordt via app.py file geupdate)
import pandas as pd
import json

# Deze methode zal een product opzoeken en alle waardes die daarbij horen printen.

def prod_lookup(prod_name):

    data = pd.read_json("NutrientDatasetDictBarcode.json", 'r')

    df = pd.DataFrame(data)
    
    testdf = df.copy()

    prod_name = prod_name.upper()

    
    prod_name = prod_name.split()
    
    print(len(prod_name))

    for i, product in testdf.iterrows(): 
        if len(prod_name) == 1:
            if prod_name[0] in product["ShortDescrip"]:
                print(str(product))
        elif len(prod_name) == 2:
            if prod_name[0] in product["ShortDescrip"] and prod_name[1] in product["ShortDescrip"]:
                print(str(product))
        elif len(prod_name) == 3:
            if prod_name[0] in product["ShortDescrip"] and prod_name[1] in product["ShortDescrip"] and prod_name[2] in product["ShortDescrip"]:
                print(str(product))
        elif len(prod_name) == 4:
            if prod_name[0] in product["ShortDescrip"] and prod_name[1] in product["ShortDescrip"] and prod_name[2] in product["ShortDescrip"] and prod_name[3] in product["ShortDescrip"]:
                print(str(product))
     

prod_lookup("butter with salt")