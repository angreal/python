import os
import subprocess

import angreal


@angreal.command(name="clean", about="cleans out generated cruft")
def run_tests():
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
