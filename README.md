### Setup

* Create a virtual environment

    python3 -m venv venv

* Activate the environment

    . venv/bin/activate

* Install the packages required

    pip install -r requirements.txt

* set the configuration for the app (change accordingly to your local environment)

    cp environments/.env .env

### Running the  App

export FLASK_APP=app
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=4000

### Deploy to heroku

* pip install gunicorn

* create Procfile in root of the application with the following

* Set **Config Vars** in settings of the app which contains .env fields with heroku app envionment settings

```
web: gunicorn samchitam_ui:app
```

* **samchitam_ui** is the name of the module
* **app** is the name of the app 