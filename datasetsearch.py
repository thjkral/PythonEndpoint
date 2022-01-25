import pandas as pd
import json

# data = pd.read_json("NutrientDatasetDictBarcode.json", 'r')

# df = pd.DataFrame(data)

# testdf = df.copy()

# print(testdf["FoodGroup"].unique())

# def product_search(productname, foodgroup):

#     for i, product in testdf.iterrows():
#         if productname in product["ShortDescrip"] and foodgroup in product["FoodGroup"]:
#             print(str(product))
#             return(str(product))

# product_search()

# def prod_lookup(prod_name):

#     data = pd.read_json("NutrientDatasetDictBarcode.json", 'r')

#     df = pd.DataFrame(data)
    
#     testdf = df.copy()

#     prod_name = prod_name.upper()

    
#     prod_name = prod_name.split()

#     for i, product in testdf.iterrows(): 
#         if len(prod_name) == 1:
#             if prod_name[0] in product["ShortDescrip"]:
#                 print(str(product))
#         elif len(prod_name) == 2:
#             if prod_name[0] in product["ShortDescrip"] and prod_name[1] in product["ShortDescrip"]:
#                 print(str(product))
#         elif len(prod_name) == 3:
#             if prod_name[0] in product["ShortDescrip"] and prod_name[1] in product["ShortDescrip"] and prod_name[2] in product["ShortDescrip"]:
#                 print(str(product))
#         elif len(prod_name) == 4:
#             if prod_name[0] in product["ShortDescrip"] and prod_name[1] in product["ShortDescrip"] and prod_name[2] in product["ShortDescrip"] and prod_name[3] in product["ShortDescrip"]:
#                 print(str(product))
     

# prod_lookup("tomato puree")

def prod_lookup(prod_name):

    data = pd.read_json("NutrientDatasetDictBarcode.json", 'r')

    df = pd.DataFrame(data)
    
    testdf = df.copy()

    prod_name = prod_name.upper()

    prod_name = prod_name.split()

    prodList = []

    for i, product in testdf.iterrows(): 
        if len(prod_name) == 1:
            if prod_name[0] in product["ShortDescrip"]:
                prodList.append(product)                
        elif len(prod_name) == 2:
            if prod_name[0] in product["ShortDescrip"] and prod_name[1] in product["ShortDescrip"]:
                prodList.append(product)  
        elif len(prod_name) == 3:
            if prod_name[0] in product["ShortDescrip"] and prod_name[1] in product["ShortDescrip"] and prod_name[2] in product["ShortDescrip"]:
                prodList.append(product) 
        elif len(prod_name) == 4:
            if prod_name[0] in product["ShortDescrip"] and prod_name[1] in product["ShortDescrip"] and prod_name[2] in product["ShortDescrip"] and prod_name[3] in product["ShortDescrip"]:
                prodList.append(product)
    for x in range(len(prodList)):
        print(prodList[x])
    return prodList 
   
     

prod_lookup("spaghetti")

