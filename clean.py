import pandas as pd
import matplotlib.pyplot as plt

country_df = pd.read_csv("./dictionary.csv")
summer_df = pd.read_csv("./summer.csv")
winter_df = pd.read_csv("./winter.csv")

#affichage des attributs comportant des valeurs manquantes
print("Attributs avec valeurs manquantes dans dictionary.csv :")
print(country_df.isnull().sum())

print("\nAttributs avec valeurs manquantes dans summer.csv :")
print(summer_df.isnull().sum())     

print("\nAttributs avec valeurs manquantes dans winter.csv :")
print(winter_df.isnull().sum())


#calcul du pourcentage de valeurs manquantes 
total_rows = len(country_df) + len(summer_df) + len(winter_df)
print("Nombre total de lignes dans les trois fichiers : ", total_rows)

total_missing = country_df.isnull().sum().sum() + summer_df.isnull().sum().sum() + winter_df.isnull().sum().sum()
print("Nombre total de valeurs manquantes dans les trois fichiers : ", total_missing)

pourcentage_missing = (total_missing / (total_rows * len(country_df.columns))) * 100
print("Pourcentage de valeurs manquantes dans les trois fichiers : {:.2f}%".format(pourcentage_missing))


# remplacer les valeurs manquantes dans la colonne 'country' par 'Unknown'
summer_df['Country'] = summer_df['Country'].fillna('UKNOWN')

# ajout des PIB et du nombre d'habitant directement depuis le csv


total_missing_after_cleanning = country_df.isnull().sum().sum() + summer_df.isnull().sum().sum() + winter_df.isnull().sum().sum()
print("Nombre total de valeurs manquantes dans les trois fichiers : ", total_missing_after_cleanning)

