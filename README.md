# wedding_planner
Repo voor de Webtechnologie opdracht van Gavin en Anh-Thy.

## Instructies:
### 1. Clone dit op uw repository 
```bash
git clone https://github.com/GavinvdB/wedding_planner.git
```
### 2. Vul dit in uw terminal/console:
```bash
cd wedding_planner
```
### 3. Vul vervolgens dit in uw terminal om een environment te openen:
```bash
python -m venv venv
```
### 4. Activeer vervolgens uw virtual environment:
```bash
venv\Scripts\activate
```
### 5. Installeer vervolgens de benodigde packages:
```bash
pip install -r requirements.txt
```
### 6. Eerst de database intializen met:
```bash
flask --app app.py db init
```
### 7. Daarna migrate je de database naar de laatste versie:
```bash
flask --app app.py db migrate
```
### 8. Dan moet je vervolgens de database updaten:
```bash
flask --app app.py db upgrade
```
### 9. Run vervolgens seed.py of vul het onderstaande in uw terminal:
```bash
python seed.py
```
#### Er komt vervolgens een data.sqlite in uw wedding_planner map 
### 10. Run vervolgens app.py of vul dit in uw terminal:
```bash
python app.py
```

### Nu kan je de website lokaal openen!

## Admin gegevens: Voor admin specifieke routes
#### Username: admin
#### Password: admin

## Functionaliteiten:
### No user
- **Je kan een account aanmaken** via het login dropdown-menu in de navigatiebar
- **Informatie over het bedrijf staat op verschillende pagina's** die via de navigatiebar zijn te vinden 
- Je kan **gegevens invullen in een contactformulier**
### User
- Als je een **user** bent heb je een moodboard en een to-do-list in een dashboard dat **alleen toegankelijk is als je ingelogd** bent
- Er is een navigatiebar die leidt **naar specifieke routes** zoals een dashboard
### Admin
- Als **admin** heb je een moodboard en een to-do-list in een dashboard dat **alleen toegankelijk is als je ingelogd** bent
- Als admin kan je gegevens van het contactformulier **inlezen en verwijderen**
- Er is in de navigatiebar dropdown een optie die leidt naar **specifieke routes** zoals een dashboard en een database voor de contactformulieren
