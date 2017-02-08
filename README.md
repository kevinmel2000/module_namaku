# Openedoo Module Tutorial

This is an example of openedoo module. This module will return my name as json.
```
{
  "nama": "Dwi purnomo"
}
```
if you want to immediately see the result, install this module by
```
$ python manage.py module install https://github.com/dwipr/module_namaku.git
```
Or
```
$ openedoo module install https://github.com/dwipr/module_namaku.git
```

## How-to Tutorial
I assume you already know the basic of python. Create a python virtual environment in your workspace and activate it (use python 2)
```
$ virtualenv venv
$ source bin/activate
```
Clone the openedoo core.
```
$ git clone https://github.com/openedoo/openedoo.git
```
Follow the openedoo setup instruction.

then create a module
```
$ python manage.py module create -n "module_namaku"
```
it creates `modules` directory, open it and you will find a directory named `module_namaku`, this is your module development workspace. Open `__init__.py` and you will see a boilerplate module there.

i use jsonify to send the response as `application/json`. Change the boilerplate module to look like this
```
from openedoo.core.libs import blueprint
from flask import jsonify

module_namaku = blueprint('module_namaku', __name__)

@module_namaku.route('/', methods=['GET'])
def index():
    namaku = {"nama": "Dwi purnomo"}
    return jsonify(namaku)
```

Then run the openedoo server
```
$ python manage.py run
```

navigate to
```
http://127.0.0.1:5000/module_namaku
```
This is just an introductory tutorial. Let's make something awesome with openedoo.
