# django_periodiq
**django_periodiq** is a Django app that integrates with [Periodiq][periodiq].


## Requirements
* [Django][django] 2.2+
* [Periodiq][periodiq] 0.12.1+


## Installation
    pip install django-dramatiq django-periodiq
Add `django_periodiq` to installed apps *before* any of your custom
apps and *after* `django_dramatiq`:
``` python
import os

INSTALLED_APPS = [
    "django_dramatiq",
    "django_periodiq",
    "myprojectapp1",
    "myprojectapp2",
    # etc...
]
```
Add `periodiq.PeriodiqMiddleware` to `DRAMATIQ_BROKER` middlewares:
``` python
DRAMATIQ_BROKER = {
    "MIDDLEWARE": [
            ...
        "periodiq.PeriodiqMiddleware",
    ],
}
```
Run dramatiq:
```shell
python manage.py rundramatiq
````
Run periodiq:
```shell
python manage.py runperiodiq
```

[periodiq]: https://gitlab.com/bersace/periodiq
[django]: http://djangoproject.com/
