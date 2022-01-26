import pandas as pd
import json

data = pd.read_json("NutrientDatasetDictBarcode.json", 'r')

df = pd.DataFrame(data)
    
cleaningdf = df.copy()


cleaningdf["Descrip"] = cleaningdf["Descrip"].str.lower()

print(type(cleaningdf))

cleaningdf.to_json(r'NutrientDatasetDictUpdate.json')

# with open("NutrientDatasetDictUpdate.json", "w") as fp:
#     json.dump(cleaningdf, fp, indent = 4)   

# lowerword = []

# for word in cleaningdf["Descrip"]:
#     lowerword.append(word.lower().split())

# print(lowerword)




