# Based on https://github.com/Bogdanp/django_dramatiq
# Copyright (c) 2017, Bogdan Paul Popa
# All rights reserved.
import os
import subprocess
import sys

from django_dramatiq.management.commands.rundramatiq import Command as DramatiqCommand


class Command(DramatiqCommand):
    help = "Runs Periodiq process."

    def add_arguments(self, parser):
        parser.add_argument(
            "--path",
            "-P",
            default=".",
            nargs="*",
            type=str,
            help="The import path (default: .).",
        )

    def handle(self, path, verbosity, **options):
        def _write(*args, **kwargs):
            if verbosity:
                self.stdout._write(*args, **kwargs)

        self.stdout._write = self.stdout.write
        self.stdout.write = _write

        executable_name = "periodiq"
        executable_path = self._resolve_executable(executable_name)

        verbosity_args = ["-v"] * (verbosity - 1)
        tasks_modules = ["django_periodiq.setup"] + self.discover_tasks_modules()
        process_args = [
            executable_name,
            # -v -v ...
            *verbosity_args,
            # django_dramatiq.tasks app1.tasks app2.tasks ...
            *tasks_modules,
            "--path",
            *path,
        ]

        self.stdout.write(f" * Running periodiq: {' '.join(process_args)}\n\n")

        if sys.platform == "win32":
            command = [executable_path] + process_args[1:]
            sys.exit(subprocess.run(command))

        os.execvp(executable_path, process_args)
