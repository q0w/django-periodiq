import os
import sys
from io import StringIO
from unittest import mock

from django.core.management import call_command


@mock.patch("os.execvp")
def test_runperiodiq_can_run_periodiq(execvp_mock):
    buff = StringIO()
    call_command("runperiodiq", stdout=buff)

    assert (
        "Discovered tasks module: 'django_dramatiq.tasks'" in buff.getvalue()
    )
    assert (
        "Discovered tasks module: 'testing.testapp1.tasks'" in buff.getvalue()
    )

    expected_exec_name = "periodiq"
    expected_exec_path = os.path.join(
        os.path.dirname(sys.executable),
        expected_exec_name,
    )

    execvp_mock.assert_called_once_with(
        expected_exec_path,
        [
            expected_exec_name,
            "django_periodiq.setup",
            "django_dramatiq.setup",
            "django_dramatiq.tasks",
            "testing.testapp1.tasks",
            "testing.testapp2.tasks.task",
            "testing.testapp2.tasks.tasks",
            "testing.testapp2.tasks.utils",
            "testing.testapp2.tasks.utils.not_a_task",
            "--path",
            ".",
        ],
    )


@mock.patch("os.execvp")
def test_runperiodiq_can_ingore_modules(execvp_mock, settings):
    buff = StringIO()

    settings.DRAMATIQ_IGNORED_MODULES = (
        "testing.testapp1.tasks",
        "testing.testapp2.tasks.tasks",
    )

    call_command("runperiodiq", stdout=buff)

    assert "Ignored tasks module: 'testing.testapp1.tasks'" in buff.getvalue()

    expected_exec_name = "periodiq"
    expected_exec_path = os.path.join(
        os.path.dirname(sys.executable),
        expected_exec_name,
    )

    execvp_mock.assert_called_once_with(
        expected_exec_path,
        [
            expected_exec_name,
            "django_periodiq.setup",
            "django_dramatiq.setup",
            "django_dramatiq.tasks",
            "testing.testapp2.tasks.task",
            "testing.testapp2.tasks.utils",
            "testing.testapp2.tasks.utils.not_a_task",
            "--path",
            ".",
        ],
    )
