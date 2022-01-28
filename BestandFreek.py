# Below are the required librarys to run the functions in this file
import pandas as pd
import json

# This function will return a list of products and their values if the conditions meet the input of the user.

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
            pass
    
    return prodList
     

# A function to lookup a product by the barcode.

def bcode_lookup(barcode):

    data = pd.read_json("NutrientDatasetWithBarcodes.json", 'r')

    df = pd.DataFrame(data)
    
    testdf = df.copy()

    for i, product in testdf.iterrows():
        if product["Barcode"] == barcode:
            return product
        else:
            pass
           

# bcode_lookup(2056)

# A function to lookup a product by the ID code.

def id_lookup(ID):

    data = pd.read_json("NutrientDatasetWithBarcodes.json", 'r')

    df = pd.DataFrame(data)
    
    testdf = df.copy()

    for i, product in testdf.iterrows():
        if product["ID"] == ID:
            return product
        else:
            pass


# id_lookup(1019)

# Function to replace a barcode in the dataset with the barcode added in the argument.

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


# Function to search a dataset to retrieve a number of calories burned per activity/sport

def burned_calories(kg, sport, time_in_hours):

    df = pd.read_csv("CleanSportDataset.csv", delimiter = ",")

    sport = sport.lower()

    sport = sport.split()

    cal_per_kg = 0

    col_rev = "Activity, Exercise or Sport (1 hour)"

    sport_list = []

    for i, activity in df.iterrows():

        if len(sport) == 1:
                  
            if sport[0] in activity[col_rev]:
                cal_per_kg += activity["Calories per kg"]
                sport_list.append(activity)

        elif len(sport) == 2:

            if sport[0] in activity[col_rev] and sport[1] in activity[col_rev]:
                cal_per_kg += activity["Calories per kg"]
                sport_list.append(activity)

        elif len(sport) ==3:

            if sport[0] in activity[col_rev] and sport[1] in activity[col_rev] and sport[2] in activity[col_rev]:
                cal_per_kg += activity["Calories per kg"]
                sport_list.append(activity)
        elif len(sport) == 4:

            if sport[0] in activity[col_rev] and sport[1] in activity[col_rev] and sport[2] in activity[col_rev] and sport[3] in activity[col_rev]:
                cal_per_kg += activity["Calories per kg"]
                sport_list.append(activity)
        else:
            pass
    return sport_list
