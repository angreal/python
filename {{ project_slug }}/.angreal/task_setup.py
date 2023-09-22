import angreal

import os
import subprocess


dev = angreal.command_group(name="dev", about="commands for development tasks")

@angreal.command(name='setup', about="setup a development environment")
def setup_env():
    one_up = os.path.join(angreal.get_root(), '..')
    return subprocess.run(
        (
            "mkdir -p .venv/angreal_python_dev;"
            "python3 -m venv .venv/angreal_python_dev;"
            ". .venv/angreal_python_dev/bin/activate;"
            "pip install -e .[dev];"
            "pre-commit install;"
            "pre-commit run --all-files;"
        ),
        shell=True,
        cwd=one_up
    )