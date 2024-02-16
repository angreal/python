import angreal

import os
import subprocess


dev = angreal.command_group(name="dev", about="commands for development tasks")

@dev()
@angreal.command(name='setup', about="setup a development environment")
def setup():
    one_up = os.path.join(angreal.get_root(), '..')
    return subprocess.run(
        (
            "pip install uv;"
            "uv venv;"
            ". .venv/bin/activate"
            "uv pip install -e .[dev];"
            "pre-commit install;"
            "pre-commit run --all-files;"
        ),
        shell=True,
        cwd=one_up
    )

@dev()
@angreal.command(name="clean", about="cleans out generated cruft")
def clean():
    one_up = os.path.join(angreal.get_root(), "..")

    subprocess.run(
        (
        "rm -rf .mypy_cache;"
        "rm -rf .pytest_cache;"
        "rm -rf htmlcov;"
        "rm -rf test.egg-info;"
        "rm -rf .coverage;"
        "find . -type d -name '__pycache__' -exec rm -rf {} + "
        ), 
        shell=True, 
        cwd=one_up
    )


@dev()
@angreal.command(name="dist", about="build your project for distribution")
def run_tests():
    one_up = os.path.join(angreal.get_root(), "..")

    subprocess.run(
        (
        "python3 -m build --sdist --wheel --outdir dist/;"
        "uv pip install {{ package_name }}@. --no-index --find-links dist --force-reinstall"
        ), 
        shell=True, 
        cwd=one_up
    )
