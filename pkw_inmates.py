# Aufgabe 2.1: PKW-Besetzungsgrad Reisezeit

# Import der Module, Funktionen und Bibliotheken
import pandas as pd
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

# Anders PKW-Besetzungsgrad Reisezeit
# Führe eine statistische Zusammenfassung des Besetzungsgrads von Pkws durch
dataCopy['V31_PerPkw'] = pd.to_numeric(dataCopy['V31_PerPkw'], errors='coerce')
evaluate_pkw_inmates = dataCopy['V31_PerPkw'].describe()
print(evaluate_pkw_inmates)


# Erstellung des Diagramms für die berechneten Werte und Festlegen der Größe des Diagramms
fig, ax = plt.subplots(figsize=(16, 9))

# Titel für y-Achse und Werte für x-Achse
name = ["Minimum", "Maximum", "Mittelwert", "Standardabw."]
values = [evaluate_pkw_inmates['min'], evaluate_pkw_inmates['max'], evaluate_pkw_inmates['mean'], evaluate_pkw_inmates['std']]

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
ax.set_title('Numerischen Werte des Pkw-Besetzungsgrads', loc='center', fontsize=17, fontweight='bold')

# Setzt die Schriftgröße der x-Achsenbeschriftungen
ax.tick_params(axis='x', labelsize=17)

# Zeigt das Diagramm, wenn das Programm ausgeführt wird
plt.show()

