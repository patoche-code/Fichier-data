import pandas as pd

# Chemin vers le fichier CSV
file_path = 'Data_all.csv'  # Remplacez par le chemin réel de votre fichier CSV
output_file_path = 'Data_all_modified.csv'  # Chemin où vous souhaitez enregistrer le fichier modifié

# Lire le fichier CSV sans modifier les noms des colonnes
df = pd.read_csv(file_path, sep=',')

# Afficher les noms des colonnes pour vérification
print("Noms des colonnes d'origine dans le fichier CSV :")
print(df.columns)

# Fonction pour extraire les caractères à partir du 19ème caractère
def extract_chars(column_name):
    if column_name == 'UTCDateTime':
        return column_name
    return column_name[18:]

# Appliquer la fonction à chaque nom de colonne
new_column_names = [extract_chars(col) for col in df.columns]

# Renommer les colonnes dans le DataFrame
df.columns = new_column_names

# Afficher les nouveaux noms des colonnes pour vérification
print("Nouveaux noms des colonnes dans le fichier CSV :")
print(df.columns)

# Liste des mots à rechercher pour supprimer les colonnes
keywords_to_remove = ['adc', 'firmware_ver', 'hardware', 'mac_address', 'mem', 'rssi', 'Source', 'uptime']

# Supprimer les colonnes contenant les mots spécifiés
df = df.loc[:, ~df.columns.str.contains('|'.join(keywords_to_remove))]

# Afficher les noms des colonnes après suppression pour vérification
print("Noms des colonnes après suppression des colonnes contenant les mots spécifiés :")
print(df.columns)

# Enregistrer le DataFrame modifié dans un nouveau fichier CSV
df.to_csv(output_file_path, index=False)