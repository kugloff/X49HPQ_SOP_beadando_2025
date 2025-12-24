@echo off
CHCP 65001 > nul
title Film API Projekt Indító

if not exist venv (
    echo.
    echo Virtuális környezet létrehozása...
    echo.
    python -m venv venv
) else (
    echo.
    echo Virtuális környezet már létezik.
    echo.
)

echo.
echo Csomagok frissítése és telepítése...
echo.
call venv\Scripts\activate
python -m pip install --upgrade pip
pip install Flask Flask-SQLAlchemy Flask-JWT-Extended Flasgger Flask-CORS

echo.
echo Az alkalmazás indítása...
echo.
echo   AZ API ELÉRHETŐ: http://localhost:3010
echo   DOKUMENTÁCIÓ (Swagger UI): http://localhost:3010/apidocs
echo.

python app.py

pause