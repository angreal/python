import angreal
from angreal.integrations.venv import VirtualEnv

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
            ". .venv/bin/activate;"
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
        "rm -rf .ruff_cache;"
        "rm -rf htmlcov;"
        "rm -rf typing_report;"
        "rm -rf dist;"
        "rm -rf build;"
        "rm -rf *.egg-info;"
        "rm -rf .coverage;"
        "find . -type d -name '__pycache__' -exec rm -rf {} + "
        ), 
        shell=True, 
        cwd=one_up
    )


@dev()
@angreal.command(name="dist", about="build your project for distribution")
def dist():
    one_up = os.path.join(angreal.get_root(), "..")
    venv_path = os.path.join(one_up, '.venv')

    with VirtualEnv(path=venv_path, now=True) as venv:
        # NOTE: Using direct subprocess calls instead of venv.install() due to
        # apparent bug in current Angreal VirtualEnv interface causing 
        # "os.dirname not found" errors
        python_path = venv.path / "bin" / "python"
        pip_path = venv.path / "bin" / "pip"
        
        # Install build dependencies
        subprocess.run(
            f"{pip_path} install build setuptools>=64 wheel", 
            shell=True, 
            cwd=one_up
        )
        
        # Build the project
        subprocess.run(
            f"{python_path} -m build --sdist --wheel --outdir dist/", 
            shell=True, 
            cwd=one_up
        )
