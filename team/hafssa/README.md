# Quelle Q6: Google Trends ("Kino" vs. "Netflix")

Status: **geprüft, aktuell nicht im Projekt verwendet** (Stand 08.11.2026)

## Steckbrief

| Feld | Inhalt |
|---|---|
| ID | Q6 |
| Anbieter | Google |
| Link | https://trends.google.de |
| Art | quantitativ, Zeitreihe |
| Zeitraum | ab 2004 bis heute |
| Format | CSV-Export über das Download-Symbol im Diagramm |
| Inhalt | Relatives Suchinteresse (Index 0 bis 100) über die Zeit, außerdem Aufschlüsselung nach Unterregion (Bundesland) und ähnliche Suchanfragen |
| Beschaffung | manueller Export, keine automatisierten Abfragen |
| Forschungsbezug | F1: Suchinteresse an "Kino" im Vergleich zu "Netflix" als Hinweis auf das Interesse an Kino und Streaming |

## Abfrage (Reproduzierbarkeit)

| Parameter | Wert |
|---|---|
| Suchbegriffe | "Kino" + "Netflix" |
| Region | Deutschland |
| Zeitraum | 2004 bis heute |
| Kategorie | Alle Kategorien |
| Suchtyp | Websuche |
| Abrufdatum | 08.11.2026 |
| Screenshot | siehe unten |

<img width="600" alt="Google Trends: Kino und Netflix" src="https://github.com/user-attachments/assets/b5fec7eb-adea-40ad-8d54-09ebbc775692" />

<img width="350" alt="Google Trends: Aufschlüsselung nach Unterregion zu Kino und Netflix" src="https://github.com/user-attachments/assets/13d96674-1f3a-4e58-94ff-dc970b1f5a1d" />

Ein CSV-Export wurde nicht in das Repository gelegt, weil die Daten aktuell nicht verwendet werden.

## Lizenz und Nutzung

- Keine offene Lizenz (z.B. Creative Commons).
- Die Google-Hilfeseite "Trends-Daten exportieren, einbetten und zitieren" erlaubt den CSV-Export und sagt, dass Informationen aus Google Trends "gemäß den Google-Nutzungsbedingungen" verwendet werden dürfen. Bei Wiederverwendung soll klar ersichtlich sein, dass die Daten von Google stammen. Die Hilfeseite nennt als Beispiel "Datenquelle: Google Trends" mit Link zu google.com/trends. (Hilfeseite geprüft am 08.11.2026: https://support.google.com/trends/answer/4365538?hl=de)
- Die Google-Nutzungsbedingungen selbst wurden nicht im Wortlaut gelesen.
- Keine automatisierten Abfragen (z.B. inoffizielle Bibliotheken wie pytrends), nur manueller Export.

**Quellenangabe:** "Datenquelle: Google Trends (https://www.google.com/trends), Abfrage vom 08.11.2026, Suchbegriffe 'Kino' und 'Netflix', Deutschland, 2004 bis heute."

## Vollständigkeit und Qualität

- Die Werte sind ein relativer Index von 0 bis 100, kein absolutes Suchvolumen. 100 ist der höchste Wert im gewählten Zeitraum und für alle verglichenen Begriffe gemeinsam.
- Bei gemeinsamer Abfrage sind die Reihen "Kino" und "Netflix" direkt vergleichbar. Ändert man Parameter wie Zeitraum oder Begriffe, ändern sich die Skalierung und die Werte.
- Die Werte können sich zwischen Abrufen leicht unterscheiden. Deshalb: Abrufdatum und Parameter festhalten und die exportierte CSV unverändert speichern.
- Im Diagramm sind an einzelnen Zeitpunkten Linien zu sehen, die einen Hinweis darstellen sollen. Sie weisen auf Änderungen bei Google hin und können Brüche in der Reihe erklären. Der genaue Wortlaut wurde nicht geprüft und müsste vor einer Nutzung nachgelesen werden.
- Beobachtung am Screenshot: "Kino" zeigt über den ganzen Zeitraum saisonale Schwankungen und einen starken Einbruch um 2020. "Netflix" ist bis etwa 2013 nahe null und steigt danach. Genaue Werte stammen aus dem CSV, nicht aus dem Screenshot.

## Grenzen der Interpretation

- Suchinteresse bedeutet nicht Nutzung oder Besuch. Die suchinteressierte Person wird nicht in jedem Fall ein Kino auch besuchen. Zudem enthält "Kino" Suchen nach Programmen, einzelnen Kinos und Filmen, kann also mehrdeutig interpretiert werden.
- Zwei Zeitreihen, die zusammen steigen oder fallen, belegen keinen ursächlichen Zusammenhang (-> Scheinkorrelation). Ein Verdrängungseffekt zwischen Netflix und Kino lässt sich so nicht nachweisen.
- Die Reihe beruht auf Stichproben von Google-Suchanfragen. Details zur Methodik wurden nicht geprüft.

## Entscheidung

Nicht als Datenquelle verwendet, weil das Projekt bereits genug Quellen enthält. Die Prüfung bleibt zur Dokumentation im Repository. Falls die Quelle später doch verwendet wird:

1. Zwei bis drei Suchbegriffe festlegen (z.B. "Kino", "Netflix").
2. Pro Abfrage das CSV exportieren.
3. Parameter in dieser Datei ergänzen und die Hinweise im Diagramm nachlesen.
