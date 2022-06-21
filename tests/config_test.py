import dramatiq


def test_skip_delay(settings):
    periodiq_middleware = dramatiq.get_broker().middleware[-1]
    assert periodiq_middleware.skip_delay == settings.PERIODIQ_SKIP_DELAY
