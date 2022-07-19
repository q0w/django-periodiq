# django_periodiq
**django_periodiq** is a Django app that integrates with [Periodiq][periodiq].


## Requirements
* [django-dramatiq][django-dramatiq] 0.11.0+
* [Periodiq][periodiq] 0.12.1+


## Installation
    pip install django-periodiq
Add `django_periodiq` to installed apps *before* any of your custom
apps and *after* `django_dramatiq`:
``` python
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
To change `PeriodiqMiddleware.skip_delay` add `PERIODIQ_SKIP_DELAY` settings

Run dramatiq:
```shell
python manage.py rundramatiq
````
Run periodiq:
```shell
python manage.py runperiodiq
```

[periodiq]: https://gitlab.com/bersace/periodiq
[django-dramatiq]: https://github.com/Bogdanp/django_dramatiq
