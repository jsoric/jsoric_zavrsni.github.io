# jsoric.github.io
Flask blog

Infinitiy travel agency

- **--** Sastoji se od pet stranica
- **--** Na Početnoj stranici se stavljaju blogovi s njihovim sadržajem.
- **--** Na O Nama stranici je kratak opis naše tvrtke.
- **--** Na Galerija stranici su slike sa putovanja.
- **--** Na Prijava stranici je forma za prijavu korisnika.
- **--** Na Registracija stranici je forma za registraciju korisnika.
- **--** Na Subscribe stranici je forma za pretplatu na obavijesti.

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
