from invoke import task
import sys

@task
def start(ctx):
    if sys.platform == "win32":
        ctx.run("python src/othello_gui.py")
    else:
        ctx.run("python3 src/othello_gui.py", pty=True)

@task
def lint(ctx):
    ctx.run("pylint src")

@task
def format(ctx):
    ctx.run("autopep8 --in-place --recursive src")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")