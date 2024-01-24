def reset_database():
    confirm = input("Möchtest du die Datenbank zurücksetzen? (ja/nein): ")
    if confirm.lower() == 'ja':
        conn = sqlite3.connect('benutzerdaten.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM benutzer')
        conn.commit()
        print("Datenbank wurde erfolgreich zurückgesetzt.")
        conn.close()
    else:
        print("Nicht zurückgesetzt.")
        