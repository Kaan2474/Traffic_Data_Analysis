#Import der Module, Funktionen und Bibliotheken
import json

# %% Erstellen eines Dictionaries mit den Platzhaltern der Befragung

platzhalter = {

    'V1_Ge': {1: 'Weiblich',
              2: 'Männlich',
              3: 'Divers',
              0: 'Keine Angabe'},

    'V2_FB': {1: 'Architektur',
              2: 'Bauingenieurwesen',
              3: 'Geodäsie',
              4: 'Elektrotechnik',
              5: 'Maschinenbau',
              6: 'Wirtschaft'},

    'V3_VMheute': {1: 'Pkw',
                   2: 'Bus und Bahn',
                   3: 'Fahrrad',
                   4: 'Mot. Zweirad',
                   5: 'Zu Fuß',
                   6: 'Sonstiges'},

    'V4_VM_Pkw': {1: 'Fast jedes Mal',
                  2: '1 - 3 Mal pro Woche',
                  3: '1 - 3 Mal pro Monat',
                  4: 'Seltener',
                  5: 'Nie'},

    'V4_VM_Bus und Bahn ': {1: 'Fast jedes Mal',
                            2: '1 - 3 Mal pro Woche',
                            3: '1 - 3 Mal pro Monat',
                            4: 'Seltener',
                            5: 'Nie'},

    'V4_VM_Fahrrad ': {1: 'Fast jedes Mal',
                       2: '1 - 3 Mal pro Woche',
                       3: '1 - 3 Mal pro Monat',
                       4: 'Seltener',
                       5: 'Nie'},

    'V4_VM_Motorisiertes Zweirad ': {1: 'Fast jedes Mal',
                                     2: '1 - 3 Mal pro Woche',
                                     3: '1 - 3 Mal pro Monat',
                                     4: 'Seltener',
                                     5: 'Nie'},

    'V4_VM_zu Fuß ': {1: 'Fast jedes Mal',
                      2: '1 - 3 Mal pro Woche',
                      3: '1 - 3 Mal pro Monat',
                      4: 'Seltener',
                      5: 'Nie'},

    'V4_VM_Sonstiges': {1: 'Fast jedes Mal',
                        2: '1 - 3 Mal pro Woche',
                        3: '1 - 3 Mal pro Monat',
                        4: 'Seltener',
                        5: 'Nie'},

    'V7_Grund_Zeitersparnis ': {1: 'Ja',
                                0: 'Nein'},

    'V7_Grund_finanzielle': {1: 'Ja',
                             0: 'Nein'},

    'V7_Grund_Andere Verkehrsmittel ': {1: 'Ja',
                                        0: 'Nein'},

    'V7_Grund_Reisekomfort': {1: 'Ja',
                              0: 'Nein'},

    'V7_Grund_Flexibilität': {1: 'Ja',
                              0: 'Nein'},

    'V7_Grund_Umweltaspekte': {1: 'Ja',
                               0: 'Nein'},

    'V7_Grund_Sonstige': {1: 'Ja',
                          0: 'Nein'}

}

#Speichern und schreiben als JSON-Datei
with open('platzhalter.json', 'w') as f:
    json.dump(platzhalter, f)

