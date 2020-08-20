:: make.bat

@ECHO OFF

pushd %~dp0

:: Set up the env vars. From .env.example
:: set FLASK_APP=autoapp.py
:: Commented the above out because I wanted to move it to the standard app.py
set FLASK_DEBUG=1
set FLASK_ENV=development
set DATABASE_URL=sqlite:///./dev.db
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

:: check that this worked
echo "Your python environment is: "
echo %conda_prefix%

:: So if they give the parameter "env" only activate stuff but don't start it
:: similar to pipenv shell
if "%1" == "env" goto end

:: otherwise use the package.json start script to initialize the server.
:: note: this needs to be installed with `yarn install` beforehand
:: alternatively `flask run` would work here; however, we want webpack to build stuff too
yarn start

:end
popd
