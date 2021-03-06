## ❗ Achtung ❗
Dieses Repository ist eine Auftragsarbeit für ein Forschungsprojekt der Universität Hamburg und hat nur sehr begrenzte Anwendungsgebiete darüber hinaus. Weil das spezifische Format, das hier geparsed wird, auch noch in weiteren Kontexten verwendet wird ist die Dokumentation hier trotzdem so ausführlich. Für die generelle Stapelverarbeitung von txt-Dateien in Excel-Tabellen ist dieses Skript nicht geeignet.

## Changelog
#### Version 1.1.0 
* Das Skript wirft keine Fehler mehr wenn bestimmte Felder nicht befüllt sind oder nicht existieren
* Die Excel-Datei wird mit Zeitstempeln aus der im Package integrierten CSV-Datei befüllt

#### Version 1.1.1
* Der Ordner `data/` wurde bei der Installation nicht mit installiert

#### Version 1.2.0
* Output-Dateien sind nun standardmäßig formatiert (Überschriften, Spaltenbreiten)
* Date und Time werden zu einem Feld zusammengeführt, Excel erkennt den Datentyp nun direkt
* Sortierung ist nun in der Output-Datei voreingestellt (muss von Hand aktiviert werden)

#### Version 1.2.1
* Problem mit Datums-Datei behoben: Ein Eintrag hatte eine falsch formatierte Uhrzeit

## Installation
### Via brew (macOS)
#### Schritt 1: Homebrew installieren
Wenn Homebrew noch nicht installiert ist, dann Homebrew nach der [offiziellen Anleitung](https://brew.sh/) installieren.

#### Schritt 2: Repository zu Homebrew hinzufügen
Dieses Repository im Terminal als Tap hinzufügen:
`brew tap Johnderate/txt-to-excel`
Dadurch erkennt Homebrew die Formel aus diesem Repository und kann die Software installieren. Sollte `brew tap` zum ersten mal genutzt werden, fragt das Programm nach GitHub-Zugangsdaten, die man im Zweifelsfall noch anlegen muss. Diese einfach eingeben, dass bei der Eingabe des Passworts nichts zu sehen ist dient der Sicherheit und ist normal.

#### Schritt 3: Formel installieren
Da Homebrew diese Formel nun kennt, kann sie wie eine normale Homebrew-Formel installiert werden. Dabei werden auch alle nötigen Abhängigkeiten installiert.
`brew install txt-to-excel`

### Manuell (macOS, Linux – für Fortgeschrittene)
txt-to-excel.py kann auch manuell installiert werden, indem es in ein dem Path hinzugefügtes Directory kopiert wird. Dann muss die Abhängigkeit `openpyxl`, die nicht Teil der standard Python Installation ist, manuell über pip installiert werden. Das Skript muss dann manuell auf dem neuesten Stand gehalten werden. Der jeweils aktuelle Stand des main-Branches sollte immer einsatzfähig sein. Der Aufbau des Skripts folgt Python-Konventionen, allerdings sind die Abhängigkeiten nicht in der setup.py aufgelistet, da dies zu Problemen mit homebrew führt.

## Nutzung
Das Skript kann auf zwei Arten genutzt werden um Dateien zu verarbeiten:

#### Im Verzeichnis
Standardmäßig, wenn es nur als `txt-to-excel` aufgerufen wird, durchsucht es das aktuelle Verzeichnis nach txt-Dateien und parsed die. Sollen auch Unterordner mit einbezogen werden, so muss die flag `-r` mit übergeben werden.

#### Mit Input
Das Skript ist auch in der Lage, eine Liste von Dateinamen als Input zu empfangen. Das wurde vor allem entwickelt, damit die Dateien per `grep` durchsucht werden können und die Ergebnisse dieser Suche dann zu Excel verarbeitet werden können. Dabei bei grep unbedingt `-l` übergeben, damit nur die Dateinamen ausgegeben werden! Eine Einführung in `grep` würde hier zu weit führen, für den Einstieg empfehle ich aber z.B. [diese Anleitung](https://www.howtoforge.com/tutorial/linux-grep-command/).

Beispiel: `grep -rl "abcd" . | txt-to-excel` 
durchsucht das aktuelle Verzeichnis (.) und alle Unterordner (-r) nach Dateien, die den Text "abcd" enthalten und gibt eine Liste der Dateinamen aus (-l). Dieses Ergebnis wird dann mit `|` (Pipe) an txt-to-excel übergeben.

### Hilfe
Das Programm selber gibt einen Überblick über alle Funktionen und möglichen Argumente, wenn es als `txt-to-excel -h` aufgerufen wird.