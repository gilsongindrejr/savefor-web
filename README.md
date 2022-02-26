# Savefor - web

Web app to receive files uploaded by <a href="https://github.com/gilsongindrejr/savefor-desktop">savefor desktop app</a>

### Create a virtual enviroment
```
python -m venv venv
```

### Activate the enviroment

Windows (Powershell)
```
.\venv\Scripts\Activate.ps1
```

Linux
```
source venv/bin/activate
```

### Install the dependencies
```
pip install -r requirements.txt
```

### Create the migrations
```
python manage.py makemigrations
```

```
python manage.py migrate
```

### Start the server
```
python manage.py runserver
```

The app will be available at:``127.0.0.1:8000/users/login``.

### Create a account

Just access:``127.0.0.1:8000/users/register`` and fill the nedded info.

### Upload the files

When logged in, access: ``127.0.0.1:8000/upload`` select a file and click upload.
