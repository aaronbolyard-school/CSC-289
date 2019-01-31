# Photo Manager, capstone project for CSC-289
A web service that allows uploading, tagging, searching, and sharing photos.

## Install
Run these commands (assuming Windows 10 & PowerShell):

```
python -m venv venv
cmd
venv\Scripts\activate.bat
pip install flask flask_sqlalchemy flask_login wtforms
```

## Running
Run these commands:

```
cmd
venv\Scripts\activate.bat
set FLASK_APP=photomanager
set FLASK_ENV=development
flask run
```

Instead of `flask run`, there are some other commands:

* `add-admin`: Adds an admin account. Takes `--name`, `--email`, and `--password`.

Developers:
* Aaron Bolyard
* Grace Ross
* Nick Zwan
