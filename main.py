import Windows1, wx, sqlite3
#----------------------------------------------------------------------------------------------------------------------------------
# Klasse für Datenbankverwaltung (Model)
class MyDatabase(object):
    def __init__(self, name="database.db"):
        print("(Klasse Datenbank) Datenbankklasse wird initialisiert")
        self.name = name
        self.con = sqlite3.connect(self.name)   # Verbindung herstellen
        self.cur = self.con.cursor()            # Cursor (Zeiger) erstellen

        # Tabellen neu erstellen

        self.create_tables()
        # Es geht weiter ....

    def create_tables(self):
        # Tabelle Messages
        sql = """
        CREATE TABLE IF NOT EXISTS msg (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            username        VARCHAR(100) NOT NULL,
            email           VARCHAR(100) NOT NULL,
            message         TEXT NOT NULL,
            date            DATETIME DEFAULT current_timestamp
        );
        """
        self.cur.execute(sql)
        self.con.commit()

    def save_message(self, name, email, comment):
        # Message speichern
        sql = " INSERT INTO msg (username, email, message) VALUES (?, ?, ?);"

        self.cur.execute(sql, (name, email, comment))
        self.con.commit()

#----------------------------------------------------------------------------------------------------------------------------------
# Klasse für graphische Oberfläche (erbt von WXBuilder und verarbeitet )
class WorkWindows1(Windows1.MyWindow1):
    def __init__( self, parent, dbase ):
        print("(2. Klasse (abgeleitet) Hauptfenster) Abgeleitetes Hauptfenster wird initialisiert")
        super().__init__(parent)

        print("(2. Klasse (abgeleitet) Hauptfenster) Datenbankverbindug wird im abgeleiteten Hauptfenster gespeichert")
        self.dbase = dbase

    def OnBtnSaveClicked( self, event ):
        print("(2. Klasse (abgeleitet) Hauptfenster) Button Save gedrückt")   
        name = self.txtctl_name.GetValue()
        email = self.txtctl_mail.GetValue()
        comment = self.txtctl_comment.GetValue()
        self.dbase.save_message(name, email, comment)

        print(f"Sie haben '{name}', '{email}' und '{comment}' eingegeben.")
        event.Skip()

    def OnBtnCancelClicked( self, event ):
        print("(2. Klasse (abgeleitet) Hauptfenster) Button Cancel gedrückt")
        self.txtctl_name.SetValue("")
        self.txtctl_mail.SetValue("")
        self.txtctl_comment.SetValue("")
        event.Skip()

#----------------------------------------------------------------------------------------------------------------------------------
# Klasse für Verarbeitung (Controling)
class MainApp(wx.App):
    def OnInit(self):
       print("(App-Klasse) App wird initialisiert")

       print("(App-Klasse) Erstelle Datenbankverbindung")
       self.dbase1 = MyDatabase() 
       
       print("(App-Klasse) Initialisier Fenster")                        # Objekt für Datnbankklasse wird erstellt
       self.fenster1 = WorkWindows1(None, self.dbase1)      # Objekt für graphische Obefläche wird erstellt

       print("(App-Klasse) Zeige Fenster an")
       self.fenster1.Show(True)                             # Fenster wird angezeigt
       return True

#----------------------------------------------------------------------------------------------------------------------------------
# Startet App-KLasse wenn das laufende Modul das Startmodul (__main__) ist
if __name__ == '__main__':
    print("(Main) Hauptprogramm")
    app = MainApp()
    print("(Main) Warte und bearbeite Ereignisse (Events)")
    app.MainLoop()