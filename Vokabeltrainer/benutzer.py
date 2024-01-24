#Benutzerklasse mit Punktestand-Funktionen

class Benutzer:                             #Klasse des Benutzers
    def __init__(self, benutzername):       #Benutzer hat den Konstruktor __init__ mit einem Parameter
        self.benutzername = benutzername    #Parameter als Attribute des Benutzer Objekts speichern
        self.punktzahl = 0                  #Parameter Punktzahl beginnend mit 0 erstellen

    def punkt_hinzufuegen(self, punkte):    #Funktion: Punkte hinzufügen zum Punktestand
        self.punktzahl += punkte            #Parameter Punktzahl