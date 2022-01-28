import pandas as pd
import json

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
    for x in range(len(prodList)):
        return prodList[x]

# print(prod_lookup("babyfood apples dices"))

# def barcode_modifier(new_barcode, prod_name):

#     data = pd.read_json("NutrientDatasetDictUpdate.json", 'r')

#     df = pd.DataFrame(data)
    
#     testdf = df.copy()

#     prod_name = prod_name.upper()

#     new_values = []

#     for i, x in testdf.head().iterrows():
#         if prod_name in x["ShortDescrip"]:
#             x = x.replace(x["Barcode"], new_barcode)
#             testdf.loc[i] = x
#             print(x["Barcode"])
    
# # barcode_modifier(8710400044567, "TOMATO PRODUCTS,CND,PUREE,W/SALT")
# # barcode_modifier(8718907108324, "CHILI WITH BEANS,CANNED")
# # barcode_modifier(3083680597210, "CORN,SWT,WHITE,CKD,BLD,DRND,W/SALT")
# # barcode_modifier(8000050837825, "SPAGHETTI,CKD,ENR,W/ SALT")
# # barcode_modifier(111111222222, "BUTTER,WITH SALT")

data = pd.read_json("NutrientDatasetDictUpdate.json", 'r')

df = pd.DataFrame(data).set_index("ID")

testdf = df.copy()

new_values = []

for i, product in testdf.iterrows():
    if product["ShortDescrip"] == '"BUTTER,WITH SALT"':
        new_object = product.replace(product["Barcode"], 111111222222)
        new_barcode = new_object["Barcode"]
        new_values.append(new_barcode)
    elif product["ShortDescrip"] == '"SPAGHETTI,CKD,ENR,W/ SALT"':
        new_object = product.replace(product["Barcode"], 8000050837825)
        new_barcode = new_object["Barcode"]
        new_values.append(new_barcode)        
    elif product["ShortDescrip"] == '"CORN,SWT,WHITE,CKD,BLD,DRND,W/SALT"':
        new_object = product.replace(product["Barcode"], 3083680597210)
        new_barcode = new_object["Barcode"]
        new_values.append(new_barcode)  
    elif product["ShortDescrip"] == '"CHILI WITH BEANS,CANNED"':
        new_object = product.replace(product["Barcode"], 8718907108324)
        new_barcode = new_object["Barcode"]
        new_values.append(new_barcode) 
    elif product["ShortDescrip"] == '"TOMATO PRODUCTS,CND,PUREE,W/SALT"':
        new_object = product.replace(product["Barcode"], 8710400044567)
        new_barcode = new_object["Barcode"]
        new_values.append(new_barcode) 
    else:
        new_values.append(product["Barcode"])



testdf["Barcode"] = new_values

testdf.to_json(r'NutrientDatasetWithBarcodesV2.json')












