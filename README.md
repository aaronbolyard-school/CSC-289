# Photo Manager, capstone project for CSC-289
A web service that allows uploading, tagging, searching, and sharing photos.

## Install
Run these commands (assuming Windows 10 & PowerShell):

```
python -m venv venv
cmd
venv\Scripts\activate.bat
pip install flask flask_sqlalchemy flask_login flask_wtf flask_bootstrap
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

You must add an `instance/settings.cfg`. Here is an example:

```
SECRET_KEY='hotpotato123'
SQLALCHEMY_DATABASE_URI='sqlite:///../instance/www.db'
```

Basically, you need to set `SECRET_KEY` and `SQLALCHEMY_DATABASE_URI`.

Instead of `flask run`, there are some other commands:

* `add-admin`: Adds an admin account. Takes `--name`, `--email`, and `--password`.

## Branching / Git
There is a PR process.

Create a branch with your new code:

```
git checkout master
git pull origin
git checkout -B name-of-branch
```

(Where name-of-branch is something like `feature-add-login` or `fix-change-password`).

Commit your could as usual.

Then create a pull request when the addition is complete. One other person must review it to commit it to master.

Developers:
* Aaron Bolyard
* Grace Ross
* Nick Zwan
