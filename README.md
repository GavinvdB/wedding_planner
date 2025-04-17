# wedding_planner
Repo voor de Webtechnologie opdracht van Gavin en Anh-Thy

## Inhoudsopgave
- [Installatie Instructies](#instructies)
  - [Optie A](#1a-clone-dit-op-jouw-repository)
  - [Optie B](#1b-download-het-zipbestand-dan-unzippen-en-openen-in-jouw-editor)
- [Admin Inloggegevens](#admin-gegevens-voor-admin-specifieke-routes)
- [Features](#functionaliteiten)
  - [Guest Features](#no-user)
  - [User Features](#user)
  - [Admin Features](#admin)

## Instructies:
## Optie A: Repository clonen
### 1a. Clone dit op jouw repository: 
```bash
git clone https://github.com/GavinvdB/wedding_planner.git
```
### 2a. Vul dit in jouw terminal/console:
```bash
cd wedding_planner
```
## Optie B: Zip.bestand downloaden
### 1b. Download het zip.bestand, dan unzippen en openen in jouw editor
### 2b. Vul dit in jouw terminal/console:
```bash
cd wedding_planner-main
```
## Volg vervolgens deze stappen
### 3. Vul vervolgens dit in jouw terminal om een environment te openen:
```bash
python -m venv venv
```
### 4. Activeer vervolgens jouw virtual environment:
```bash
venv\Scripts\activate
```
### 5. Installeer vervolgens de benodigde packages:
```bash
pip install -r requirements.txt
```
### 6. Eerst de database initialiseren met:
```bash
flask --app app.py db init
```
### 7. Daarna migreer je de database naar de laatste versie:
```bash
flask --app app.py db migrate
```
### 8. Dan moet je vervolgens de database updaten:
```bash
flask --app app.py db upgrade
```
### 9. Run vervolgens seed.py of vul het onderstaande in jouw terminal:
```bash
python seed.py
```
#### Er komt vervolgens een data.sqlite in jouw wedding_planner map 
### 10. Run vervolgens app.py of vul dit in jouw terminal:
```bash
python app.py
```

### Nu kan je de website lokaal openen!

## Admin gegevens: Voor admin specifieke routes
#### Username: admin
#### Password: admin

## Functionaliteiten:
### Guest
- **Je kan een account aanmaken** via het login dropdown-menu in de navigatiebar
- **Informatie over het bedrijf staat op verschillende pagina's** die via de navigatiebar zijn te vinden 
- Je kan **gegevens invullen in een contactformulier**
### User
- Als **user** heb je een dashboard dat **alleen toegankelijk is als je ingelogd** bent
- Er is een navigatiebar die leidt **naar specifieke routes** zoals een dashboard
### Admin
- Als **admin** heb je een dashboard dat **alleen toegankelijk is als je ingelogd** bent
- Als admin kan je gegevens van het contactformulier **inlezen en verwijderen**
- Er is in de navigatiebar dropdown een optie die leidt naar **specifieke routes** zoals een dashboard en een database voor de contactformulieren
