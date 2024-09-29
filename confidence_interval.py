# Aufgabe 1.2: Konfidenzintervall Rad

# Import der Module, Funktionen und Bibliotheken
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
from statsmodels.stats.proportion import proportion_confint

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

# Anders Konfidenzintervall

# Angabe von alpha
alpha = 0.05

# Erstellen eines leeren Dataframes
evaluate_bycicle = pd.DataFrame()

# Eintrag der value_counts
evaluate_bycicle['Anzahl'] = dataCopy['V3_VMheute'].value_counts()

# Erstellen einer Kopie zur berechnung des KI
K_int = evaluate_bycicle.copy()

# Aussortieren falscher/fehlender Angaben
if 'Angabe fehlerhaft/fehlt' in K_int.index:
    K_int = K_int.drop('Angabe fehlerhaft/fehlt')

# Berechnen der Stichprobengröße
n = sum(K_int.values)

# Berechnen der Konfidenzintervalle
K_confint = proportion_confint(K_int, n, alpha)

# Berechnen der prozentualen Anteile, aufnehmen der unteren und oberen Grenzen
K_int['Anteil'] = np.round((K_int['Anzahl'] * 100) / n, 1)
K_int['KI oben'] = np.round(K_confint[0].values, 2)
K_int['KI unten'] = np.round(K_confint[1].values, 2)

# Kombinieren und neu sortieren der Arbeitskopie mit Auswertung_Ge, ersetzen der nan-Werte
K_int = evaluate_bycicle.combine_first(K_int)
K_int.fillna(0, inplace=True)
evaluate_bycicle = K_int.reindex(evaluate_bycicle.index)
print(evaluate_bycicle)

# Erstellung des Diagramms für die berechneten Werte und Festlegen der Größe des Diagramms
fig, ax = plt.subplots(figsize=(16, 9))

# Titel für y-Achse und Werte für x-Achse
name = ["Anteil", "KI oben", "KI unten"]
values = [evaluate_bycicle["Anteil"]["Fahrrad"], evaluate_bycicle["KI oben"]["Fahrrad"], evaluate_bycicle["KI unten"]["Fahrrad"]]

# Erstellt die Balken in dem Diagramm
ax.barh(name, values, color="orange")

# Invertiert die Balken in dem Diagramm von hinten nach vorne
ax.invert_yaxis()

# Fügt hinter die Balken die Werte hinzu --> z.B Standardabweichung 28
for i in ax.patches:
    plt.text(i.get_width()+0.2, i.get_y()+0.5,
             str(round((i.get_width()), 2)),
             fontsize=17, fontweight='bold',
             color='black')

# Setzt die Schriftgröße der y-Achsenbeschriftungen
ax.set_yticklabels(name, fontsize=17, fontweight='bold')

# Fügt den Titel für das Diagramm hinzu
ax.set_title('Anteil Rad inkl. Konfidenzintervall ', loc='center', fontsize=17, fontweight='bold')

# Setzt die Schriftgröße der x-Achsenbeschriftungen
ax.tick_params(axis='x', labelsize=17)

# Zeigt das Diagramm, wenn das Programm ausgeführt wird
plt.show()