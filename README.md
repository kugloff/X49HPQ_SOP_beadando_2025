# Filmek - Saját Lista API

Ez egy **Python (Flask)** alapú RESTful API, amely lehetővé teszi filmek és sorozatok gyűjteményének kezelését. A projekt támogatja a teljes körű **CRUD** műveleteket, **JWT alapú hitelesítéssel** védett végpontokkal és interaktív **Swagger** dokumentációval rendelkezik.

## Funkciók
* **Filmkezelés:** Filmek hozzáadása, listázása, módosítása és törlése.
* **JWT Hitelesítés:** Védett végpontok (POST, PUT, DELETE), amelyek csak érvényes tokennel érhetők el.
* **Saját Lista állapot:** Nyomon követhető, hogy egy film szerepel-e a gyűjteményben (`in_my_list`).
* **Dokumentáció:** Swagger UI a könnyű teszteléshez.

* **Keretrendszer:** Flask
* **Adatbázis:** SQLite (Flask-SQLAlchemy ORM)
* **Hitelesítés:** Flask-JWT-Extended
* **Dokumentáció:** Flasgger (Swagger UI)
* **CORS:** Flask-CORS

## Projektfelépítés
* `app.py` – Az alkalmazás logikája, az adatbázis modell és a végpontok.
* `swagger.yaml` – Az API specifikációja (OpenAPI/Swagger 2.0).
* `run.bat` – Automata környezetbeállító és indító fájl Windows-ra.
* `sajatlista.db` – Az SQLite adatbázis fájl (az első indításkor jön létre).

## Telepítés és Futtatás
### 1. Automata indítás
Futtasd a mappában található **run.bat** fájlt. Ez:
1.  Létrehozza a virtuális környezetet (`venv`).
2.  Telepíti a szükséges könyvtárakat (`Flask`, `SQLAlchemy`, stb.).
3.  Elindítja a szervert a **3010**-es porton.
---

## API Használat

Az API indítása után a vizuális dokumentáció az alábbi címen érhető el:
[http://localhost:3010/apidocs](http://localhost:3010/apidocs)

### Végpontok áttekintése

| Metódus | Végpont | Leírás | Hitelesítés |
| :--- | :--- | :--- | :--- |
| **POST** | `/login` | Bejelentkezés (admin/admin) -> Token igénylése | Nyilvános |
| **GET** | `/sajatlista` | Az összes film lekérdezése az adatbázisból | Nyilvános |
| **POST** | `/sajatlista` | Új film felvétele a listára | **JWT Token** |
| **PUT** | `/sajatlista/{film_id}` | Meglévő film adatainak frissítése | **JWT Token** |
| **DELETE** | `/sajatlista/{film_id}` | Film végleges törlése | **JWT Token** |

---

### 🔑 Hitelesítés folyamata (Swagger teszteléshez)
1.  Nyisd meg a **/login** végpontot a Swaggerben.
2.  Használd az **admin / admin** párost a bejelentkezéshez.
3.  Másold ki a kapott **access_token** értékét.
4.  Kattints a lap tetején lévő **Authorize** gombra.
5.  Írd be a mezőbe: `Bearer <kapott_token>`
6.  Most már elérhetővé válnak a védett (lakattal jelölt) műveletek.

---
*Készült a SOP beadandó keretében.*