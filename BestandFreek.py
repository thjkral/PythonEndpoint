# hierin functies maken die je op een bepaalde endpoint wilt laten zien. (deze functie wordt via app.py file geupdate)
import pandas as pd

data = pd.read_json("NutrientDatasetDict.json")

df = pd.DataFrame(data)

tstdf = df.copy()

testdf = tstdf.head(20)

# Deze methode zal een product opzoeken en alle waardes die daarbij horen printen.

def prod_lookup(prod_name, dataframe = testdf):

    prod_name = prod_name.upper()

    for i, product in dataframe.iterrows():
        if prod_name in product["ShortDescrip"]:
            return product

prod_lookup("butter,with")