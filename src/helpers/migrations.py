import subprocess

def migrations():
    revision_command = ['alembic', 'revision', '--autogenerate', '-m', 'Create tables']
    subprocess.run(revision_command, check=True)
    upgrade_command = ['alembic', 'upgrade', 'head']
    subprocess.run(upgrade_command, check=True) 