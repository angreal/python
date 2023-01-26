import os
import subprocess

import angreal


@angreal.command(name="dist", about="build your project for distribution")
def run_tests():
    one_up = os.path.join(angreal.get_root(), "..")

    subprocess.run(
        (
        "python -m build --sdist --wheel --outdir dist/;"
        "pip install {{ package_name }} --no-index --find-links dist --force-reinstall"
        ), 
        shell=True, 
        cwd=one_up
    )
