from django.conf import settings
from django_dramatiq.apps import DjangoDramatiqConfig


class DjangoPeriodiqConfig(DjangoDramatiqConfig):
    name = "django_periodiq"
    verbose_name = "Django Periodiq"

    @classmethod
    def middleware_periodiqmiddleware_kwargs(cls):
        skip_delay = getattr(settings, "PERIODIQ_SKIP_DELAY", 30)
        return {"skip_delay": skip_delay}


DjangoPeriodiqConfig.initialize()
