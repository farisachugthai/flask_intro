:: make.bat

:: @ECHO OFF

pushd %~dp0

:: Set up the env vars. From .env.example
set FLASK_APP=autoapp.py
set FLASK_DEBUG=1
set FLASK_ENV=development
set DATABASE_URL=sqlite:////tmp/dev.db
set GUNICORN_WORKERS=1
set LOG_LEVEL=debug
set SECRET_KEY=not-so-secret
:: In production, set to a higher number, like 31556926
set SEND_FILE_MAX_AGE_DEFAULT=0

:: obviously this is for a conda setup on windows
:: set this up with conda install --file .\requirements\conda_windows.txt -n flask
if "%CONDA_EXE%" == "" (
    call conda.bat activate
)
call conda.bat activate flask

:: install with yarn
:: alternatively flask run but we want webpack to build stuff too
yarn start
