import sqlite3                                                                          #Importiert die Sqlite3
def reset_database():                                                                   #Definition der Funktion reset_database
    confirm = input("Möchtest du die Datenbank zurücksetzen? (ja/nein): ")              #Benutzerabfrage für das Zurücksetzen der Datenbank
    if confirm.lower() == 'ja':                                                         #Eingabe ja?
        conn = sqlite3.connect('benutzerdaten.db')                                      #Verbindung zur SQLite-Datenbank herstellen
        cursor = conn.cursor()                                                          #Cursor erstellen, um mit der Datenbank zu interagieren
        cursor.execute('DELETE FROM benutzer')                                          #SQL-Befehl zum Löschen aller Einträge in der Tabelle 'benutzer'
        conn.commit()                                                                   #Änderungen in der Datenbank bestätigen
        print("Datenbank wurde erfolgreich zurückgesetzt.")                             #Print Bestätigung
        conn.close()                                                                    #Verbindung schließen
    else:                                                                               #Wenn nicht ja, dann nicht zurücksetzen
        print("Nicht zurückgesetzt.")
