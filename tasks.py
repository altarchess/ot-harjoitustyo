from invoke import task
import sys

@task
def start(ctx):
    if sys.platform == "win32":
        ctx.run("python src/othello-gui.py")
    else:
        ctx.run("python3 src/othello-gui.py", pty=True)


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")