import nox


@nox.session(python=["3.7", "3.8", "3.9"])
@nox.parametrize("django", ["2.2", "3.0", "3.2"])
def tests(session, django):
    session.install("-r", "requirements-dev.txt")
    session.install(f"django=={django}")
    session.run("coverage", "erase")
    session.run("coverage", "run", "-m", "pytest")
    session.run("coverage", "combine")
    session.run("coverage", "report")


@nox.session()
def lint(session):
    session.install("pre-commit")
    session.run("pre-commit", "run", "--all-files", "--show-diff-on-failure")
