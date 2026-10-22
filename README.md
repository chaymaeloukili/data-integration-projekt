# Zurück auf die große Leinwand? 🎬
### Kinobesuche in Deutschland zwischen Streaming, Corona und dem Wunsch nach Erlebnis (2000–2025)

Gruppenprojekt im Modul **DIS 3.3 Data Integration** (Timo Breuer), TH Köln, Wintersemester 2026/27

> ⚠️ **Status: Entwurf (Stand 22.10.2026).** Thema, Forschungsfragen und Plan werden bis zur Roadmap-Abgabe am **13.11.2026** in der Gruppe abgestimmt.

---

## 👥 Team

| Name | GitHub |
|---|---|
| Ülkü Arslan | @[GitHub-Name] |
| Hafssa Zainou | @[GitHub-Name] |
| Aqsa Shaikh | @[GitHub-Name] |
| Chaymae Loukili | @chaymaeloukili |

---

## 💡 Thema und Motivation
 
Lange galt das Kino als Verlierer der Digitalisierung: Mit dem Start großer Streaming-Dienste in Deutschland (Netflix ab 2014) wurde Filmeschauen zu Hause immer bequemer, und die Corona-Pandemie hat die Kinos 2020/21 monatelang geschlossen. Inzwischen steigen die Besuchszahlen wieder: 2025 wurden in Deutschland 91,9 Mio. Kinotickets verkauft, mehr als im Vorjahr.
 
Uns interessiert, **wie sich der Kinobesuch in Deutschland seit 2000 verändert hat** und ob sich hinter der Erholung ein Trend verbirgt: Suchen Menschen wieder bewusst das gemeinsame, „echte“ Erlebnis vor der großen Leinwand? Eine aktuelle Studie der Filmförderungsanstalt (FFA) beschreibt den Kinobesuch heute als bewusste Entscheidung, bei der das Ticket zum „Anker für ein gemeinsames Erlebnis“ wird.
 
Dafür verbinden wir Daten zu Kinobesuchen, Bevölkerung und Streaming-Nutzung über das gemeinsame Merkmal **Jahr**.
 
---
 
## ❓ Mögliche Forschungsfragen (noch nicht final)
 
1. **Entwicklung:** Wie haben sich die Kinobesuche in Deutschland seit 2000 entwickelt, vor allem seit dem Streaming-Boom (ab 2014) und nach Corona? Gibt es einen Zusammenhang mit der Streaming-Nutzung?
2. **Publikum:** Welche Altersgruppen tragen zur Erholung der Kinobesuche nach 2021 bei, und zeigt sich in Deutschland der in den USA berichtete Gen-Z-Trend?
3. **Erlebnis:** Entwickeln sich Programmkinos seit 2010 anders als der Gesamtmarkt?
Erste Hinweise: 2025 wuchs das Kinopublikum in Deutschland vor allem bei Menschen ab 50 Jahren, während 10- bis 29-Jährige weniger Tickets kauften (FFA). Unsere Daten zeigen Zusammenhänge, aber nicht automatisch Ursachen. Wir formulieren Ergebnisse entsprechend vorsichtig.
 
---
 
## 📚 Datenquellen (aktueller Stand)
 
| ID | Quelle | Herausgeber | Inhalt | Jahre | Format | Lizenz | Status |
|---|---|---|---|---|---|---|---|
| Q1 | [Das Kinojahr](https://www.ffa.de/broschueren.html) | FFA Filmförderungsanstalt | Tickets, Umsatz, Eintrittspreise, Kinobestand | 2000–2025 | PDF | keine offene Lizenz („urheberrechtlich geschützt“) | Anfrage bei FFA gestellt |
| Q2 | [Kinobesucher*innen 2025](https://www.ffa.de/files/dokumentenverwaltung/studien%20mafo/2026/FFA_Kinobesucher_innen_2025.pdf) | FFA (Marktforschung) | Alter, Reichweite, Häufigkeit, Kino vs. Streaming | 2025 (Zeitreihen ab 2015) | PDF | keine offene Lizenz | Anfrage bei FFA gestellt |
| Q3 | [Vom Film zum Kinoerlebnis](https://www.ffa.de/files/dokumentenverwaltung/studien%20mafo/2026/Vom_Film_zum_Kinoerlebnis_Zahlen-Daten-Fakten_FKM_2026.pdf) | FFA (Marktforschung, Ipsos) | Besuchsmotive (Interviews), Tickets gesamt und Programmkinos | 2001–2025 | PDF | keine offene Lizenz | Anfrage bei FFA gestellt |
| Q4 | [Pressemitteilung „Kino muss heute mehr sein als ein Abspielort“](https://www.ffa.de/pressemitteilungen-detailseite.html?meldung=kino-muss-heute-mehr-sein-als-ein-abspielort) | FFA (Pressestelle) | Kurzfassung von Q3; nur zum Zitieren | 2026 (16.09.2026) | Webseite | keine offene Lizenz; Zitat mit Quellenangabe | geprüft ✅ |
| Q5 | [Pressemitteilung „Kinobesucher*innen 2025: Mehr Publikum – Wachstum vor allem bei Älteren“](https://www.ffa.de/pressemitteilungen-detailseite.html?meldung=ffa-studie-kinobesucherinnen-2025-mehr-publikum-wachstum-vor-allem-bei-aelteren) | FFA (Pressestelle) | Kurzfassung von Q2 (Altersgruppen); nur zum Zitieren | 2025 (28.05.2026) | Webseite | keine offene Lizenz; Zitat mit Quellenangabe | geprüft ✅ |
| Q6 | [Google Trends](https://trends.google.de) | Google | Geplant: Suchinteresse „Kino“ vs. „Netflix“ – Daten noch zu suchen | noch offen | noch offen | noch offen | wird noch gesucht und geprüft |
| Q7 | [ARD/ZDF-Medienstudie](https://www.ard-zdf-onlinestudie.de) | ARD/ZDF | Geplant: Daten zur Streaming-Nutzung – noch zu suchen | noch offen | noch offen | noch offen | wird noch gesucht und geprüft |
| Q8 | [Bevölkerung: Deutschland, Stichtag (12411-0001)](https://genesis.destatis.de/datenbank/online/statistic/12411/table/12411-0001/search/s/Rm9ydHNjaHJlaWJ1bmclMjBkZXMlMjBCZXYlQzMlQjZsa2VydW5nc3N0YW5kZXM%3D) | Statistisches Bundesamt (Destatis) | Einwohner pro Jahr → Kinobesuche pro Person | 1950–2025 | CSV | [Datenlizenz Deutschland – Namensnennung – Version 2.0](https://www.govdata.de/dl-de/by-2-0) | geprüft ✅ |
| Q9 | [Bevölkerung: Deutschland, Stichtag, Geschlecht (12411-0003)](https://genesis.destatis.de/datenbank/online/statistic/12411/table/12411-0003/search/s/Rm9ydHNjaHJlaWJ1bmclMjBkZXMlMjBCZXYlQzMlQjZsa2VydW5nc3N0YW5kZXM%3D) | Statistisches Bundesamt (Destatis) | Einwohner nach Geschlecht; Alternative zu Q8 | 1970–2025 | CSV | [Datenlizenz Deutschland – Namensnennung – Version 2.0](https://www.govdata.de/dl-de/by-2-0) | geprüft ✅ |
 
### Hinweis zu Lizenzen
 
Für die Daten der FFA haben wir keine offene Lizenz gefunden. Wir haben die FFA deshalb um Erlaubnis gebeten, die Zahlen mit Quellenangabe in diesem Repository zu nutzen. **Bis zur Antwort laden wir keine FFA-Dateien oder daraus abgeleiteten Tabellen hoch.** Die Daten von Destatis stehen unter einer offenen Lizenz und dürfen mit Quellenangabe genutzt werden.
 
### Bekannte Einschränkungen
 
- **Brüche in den Daten:** Die FFA zählt Kinos ab 2025 ohne Autokinos, Open Airs und Festivals; die Besucherstudie umfasst bis 2018 nur deutsche Staatsbürger*innen, ab 2019 alle in Deutschland lebenden Menschen; die Definition „Programmkino“ wurde 2009/2010 geändert; die Bevölkerungszahlen wurden nach den Zensus 2011 und 2022 neu berechnet.
- **Stichproben:** Die Besucherdaten beruhen auf einem Panel (YouGov, 20.000 Personen) und sind Hochrechnungen.
---
 
## 🗺️ Roadmap
 
| Zeitraum | Schritt | Ergebnis |
|---|---|---|
| bis 13.11.2026 | Quellen und Lizenzen klären, Forschungsfragen festlegen, Aufgaben verteilen | **Meilenstein 1: Roadmap** (diese README) |
| 13.11.–27.11.2026 | Daten herunterladen bzw. aus PDFs übertragen, Rohdaten dokumentieren | Rohdaten + Quellenliste |
| 27.11.–11.12.2026 | Daten bereinigen und über das Jahr zusammenführen (Python/pandas), z. B. Kinobesuche pro Person | erster Pipeline-Prototyp |
| bis 18.12.2026 | Angereicherten Datensatz fertigstellen und dokumentieren | **Meilenstein 2: Dataset** (World Café) |
| 08.01.–22.01.2027 | Analyse (z. B. Hypothesentests), Visualisierungen (Zeitstrahl mit Streaming-Start und Corona), Notebook | Ergebnisse + Diagramme |
| 22.01.2027, 23:59 | Letzter Commit | Repository-Deadline |
| 25.01.2027 | Präsentation mit laufendem Notebook | **Meilenstein 3: Präsentation** |
 
**Aufgabenverteilung:** wird in der Gruppe festgelegt.
 
---
 
## 🤖 Nutzung von KI
 
Wir dokumentieren jede Nutzung von KI-Werkzeugen in [`AI_USAGE.md`](AI_USAGE.md).
