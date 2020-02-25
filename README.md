# jsoric.github.io
Flask blog

Infinity travel agency je agencija za putovanja koja na **Pocetnoj stranici** prikazuje trenutne ponude sa cijenom, vrstom prijevoza i lokacijom na koje vršimo rezervacije. 

Popunjavanjem forme iz **Putuj s nama** stranice na našu bazu dolaze vaši podatci s kojim vas stavljamo na popis putnika i preko emaila obavjestavamo o daljnim uputama.

Popunjavanjem forme pretplati se dopuštate nam slanje najnovijih obavijesti o putovanjima.

- **--** Sastoji se od pet stranica
- **--** Na Početnoj stranici su lokacije na koje agencija vrši putovanja, sa slikama, cijenom i kratkim opisom.
- **--** Na O Nama stranici je kratak opis naše tvrtke.
- **--** Na Galerija stranici su slike sa putovanja.
- **--** Na Putuj s nama stranici je forma za registraciju putnika.
- **--** Na Preplati se stranici je forma za pretplatu na obavijesti.

**Podatci unešeni na Putuj s nama stranici se spremaju na sqlite bazu subscribe.db i kasnije služe za kontakt s putnikom 
  putem e-maila.**

**Podatci unešeni za pretplatu na Subscribe stranici se spremaju na sqlite bazu subscribe.db.**

Upute za instalaciju za windows korisnike

- **--** Preuzmi repozitorij

- **--** Kreiraj virtualnu okolinu I preuzmi programe u powershellu naredbom:

 **python -m venv venv**

 **venv\Scripts\Activate.ps1**

 **pip install -r requirements.txt**

 **$env:FLASK_APP = ”flaskblog.py”**

 **set FLASK\_APP=flaskblog.py**

 **$env:FLASK\_DEBUG = 1**

- **--** Pokreniti aplikaciju naredbom **flask run**
- **--** Na web browser upisati [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
