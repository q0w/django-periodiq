import dramatiq
from periodiq import cron


@dramatiq.actor(periodic=cron("* * * * *"))
def hello():
    pass
