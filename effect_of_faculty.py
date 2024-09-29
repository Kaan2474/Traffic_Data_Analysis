# Aufgabe 3.1: Einfluss von Fachbereich auf die Verkehrsmittelwahl


# Import der Module, Funktionen und Bibliotheken
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json

# Laden der Excel-Datei
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


evaluate_faculty_with_transportation = dataCopy[(dataCopy != 'Angabe fehlerhaft/fehlt')].groupby('V3_VMheute')['V2_FB']\
    .value_counts().fillna(0)
print(evaluate_faculty_with_transportation)


species = (
    'Bus und Bahn',
    'Fahrrad',
    'Mot. Zweirad',
    'Pkw',
    'Zu Fuß'
)
weight_counts = {
    'Architektur': np.array([22, 0, 1, 34, 0]),
    'Bauingenieurwesen': np.array([51, 6, 3, 52, 2]),
    'Geödäsie': np.array([10, 4, 0, 10, 1]),
    'Elektrotechnik': np.array([73, 5, 2, 24, 3]),
    'Maschinenbau': np.array([20, 2, 0, 20, 2]),
    'Wirtschaft': np.array([67, 0, 2, 48, 1])
}
width = 0.5

fig, ax = plt.subplots()
bottom = np.zeros(5)

for boolean, weight_count in weight_counts.items():
    p = ax.bar(species, weight_count, width, label=boolean, bottom=bottom)
    bottom += weight_count

ax.set_title("Einfluss des Fakultätsbereich auf die Verkehrsmittelwahl")
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=3)
# Macht die Legende sichtbar
plt.subplots_adjust(bottom=0.3)

plt.show()


"""
transportation = ('Bus und Bahn', 'Fahrrad', 'Mot. Zweirad', 'Pkw', 'Zu Fuß')
faculties_count = {
    'Architektur': np.array([22, 0, 1, 34, 0]),
    'Bauingenieurwesen': np.array([51, 6, 3, 52, 2]),
    'Geödäsie': np.array([10, 4, 0, 10, 1]),
    'Elektrotechnik': np.array([73, 5, 2, 24, 3]),
    'Maschinenbau': np.array([20, 2, 0, 20, 2]),
    'Wirtschaft': np.array([67, 0, 2, 48, 1])
}
"""