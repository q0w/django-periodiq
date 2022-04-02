import nox

nox.options.reuse_existing_virtualenvs = True
nox.options.sessions = ["lint"]


@nox.session
@nox.parametrize(
    "python,django",
    [
        (python, django)
        for python in ("3.7", "3.8", "3.9", "3.10")
        for django in ("2.2", "3.0", "3.2", "4.0")
        if (python, django) != ("3.7", "4.0")
    ],
)
def test(session: nox.Session, django: str) -> None:
    session.install("-r", "requirements-dev.txt")
    session.install(f"django=={django}")
    session.run("coverage", "erase")
    session.run("coverage", "run", "-m", "pytest")
    session.run("coverage", "combine")
    session.run("coverage", "report")


@nox.session
def lint(session: nox.Session) -> None:
    session.install("pre-commit")
    if session.posargs:
        args = session.posargs + ["--all-files"]
    else:
        args = ["--all-files", "--show-diff-on-failure"]

    session.run("pre-commit", "run", *args)
