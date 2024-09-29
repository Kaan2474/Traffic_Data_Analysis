# Aufgabe 1.1: Modal Split 2019

# Import der Module, Funktionen und Bibliotheken
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json

# Laden der Excel-Datei
data = pd.read_excel('MVP_Befragung_2019.xlsx', header=1)
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
        # Umwandeln der Platzhalter in die Bezeichnungen
        dataCopy[column] = dataCopy[column].astype(int, errors='ignore').astype(str)
        # Ersetzen der Platzhalter
        dataCopy[column] = dataCopy[column].replace(platzhalter[column])
        # Ersetzen falscher/fehlender Eingaben
        for j in dataCopy[column]:
            if j not in platzhalter[column].values():
                dataCopy[column] = dataCopy[column].replace({j: 'Angabe fehlerhaft/fehlt'})

# Anders
# Erstellen der value_counts(also die Gesamtanzahl), hier für die Spalte V3_VMheute --> Verkehrsmittel Heute 2019
evaluate_transportation = dataCopy['V3_VMheute'].value_counts()
print(evaluate_transportation)


# Berechnet die Prozentangaben des Kuchendiagramms
def calculate_percentage(data):
    whole = 0
    for i in range(len(data)):
        whole += data.iloc[i]
    for i in range(len(data)-1):
        cake_diagram_data.append(100*data.iloc[i]/whole)


# Daten für das Kuchendiagramm
cake_diagram_data = []
calculate_percentage(evaluate_transportation)
cake_diagram = np.array(cake_diagram_data)

# Beschriftungen und Hervorherbung des Kuchendiagramms
mylabels = ["Bus und Bahn", "Pkw", "Fahrrad", "Zu Fuß", "Mot. Zweirad", "Sonstiges"]
# Betonung von Bus und Bahn
explode = [0.1, 0, 0, 0, 0, 0]

# Erzeugt das Kuchendiagramm
plt.pie(cake_diagram, explode=explode, labels=mylabels, autopct='%1.1f%%', shadow=True)
plt.show()
