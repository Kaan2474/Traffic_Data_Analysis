#Aufgabe 3.1: Einfluss von Geschlecht auf die Verkehrsmittelwahl


#Import der Module, Funktionen und Bibliotheken
import pandas as pd
import matplotlib.pyplot as plt
import json

#Laden der Excel-Datei
data = pd.read_excel('MVP2024_Befragung_GesamteDatei.xlsx', header=0)
# Erstellen einer Arbeitskopie
dataCopy = data.copy()

# Bereinigen des Datensatzes und einfügen der Platzhalter

# Importieren der Platzhalter-Datei
with open('platzhalter.json', 'r') as f:
    platzhalter = json.load(f)


# Schleife über die Spaltennamen
for column in dataCopy.columns:
    # Abfrage, ob Spaltenname in Platzhalter vorkommt
    if column in platzhalter.keys():
        # Ersetzen der nicht vorhandenen Werte
        dataCopy.fillna({column: -999}, inplace=True)
        # Umwandeln der Platzhalter in strings
        dataCopy[column] = dataCopy[column].astype(int, errors='ignore').astype(str)
        # Ersetzen der Platzhalter
        dataCopy[column] = dataCopy[column].replace(platzhalter[column])
        # Ersetzen falscher/fehlender Eingaben
        for j in dataCopy[column]:
            if j not in platzhalter[column].values():
                dataCopy[column] = dataCopy[column].replace({j: 'Angabe fehlerhaft/fehlt'})


evaluate_gender_with_transportation = dataCopy[(dataCopy != 'Angabe fehlerhaft/fehlt')].groupby('V3_VMheute')['V1_Ge']\
    .value_counts().unstack().fillna(0).drop('Keine Angabe', axis=1)
print(evaluate_gender_with_transportation)

# Ändern der Spaltenreihenfolge nach Wunsch
Reihenfolge = ['Männlich', 'Weiblich', 'Divers']
evaluate_gender_with_transportation = evaluate_gender_with_transportation.reindex(columns=Reihenfolge)
labels = evaluate_gender_with_transportation.columns

colors = ['lime', 'pink', 'orange']

# Plotqualität
plt.rcParams["figure.dpi"] = 300

# Plotten der gestapelten Säulen
evaluate_gender_with_transportation.plot(kind='bar', stacked=True, color=colors,
           edgecolor='black', width=0.9, figsize=(10, 8))

plt.xticks(rotation=45, ha='right', fontsize=16)
plt.yticks(fontsize=16)
plt.title('Einfluss des Geschlechts auf die Verkehrsmittelwahl', fontsize=18)
plt.legend(labels, ncol=3, loc = 'center', bbox_to_anchor=(0.5, -0.5), fontsize=16)
plt.xlabel('')
plt.tight_layout()
plt.show()