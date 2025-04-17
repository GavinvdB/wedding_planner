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

### 1. Initialize the Database
To initialize the database, run the following command:
```bash
flask --app app.py db init
```

### 2. Migrate the Database
Migrate the database schema to the latest version with:
```bash
flask --app app.py db migrate
```

### 3. Upgrade the Database
Apply the migration to update the database with:
```bash
flask --app app.py db upgrade
```

### 6. Run vervolgens seed.py of vul het onderstaande in uw terminal:
```bash
python seed.py
```

#### Er komt vervolgens een data.sqlite in uw wedding_planner map 

### 7. Run vervolgens app.py of vul dit in uw terminal:
```bash
python app.py
```

backup in de zip met de venv + db

## Admin gegevens:
#### Username: admin
#### Password: admin

## Functionaliteiten:

### User
Als je een user/admin bent heb je een moodboard en een to do list in een dashboard dat alleen toegankelijk is als je ingelogd 
Er is een navigatiebar die leidt naar specifieke routes zoals een dashboard

### Admin
Als admin kan je gegevens van de Contactformulier inlezen en verwijderen

Er is een navigatiebar die leidt naar specifieke routes zoals een dashboard en een database voor de contactformulieren
### No user
Je kan een account aanmaken via de login drop menu in de navigatiebar

Informatie over het bedrijf staat op verschillende paginas dat via de navigatiebar is te vinden zonder account

Je kan gegevens invullen in een Contactformulier met en zonder account