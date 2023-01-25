import os
import subprocess
import webbrowser
import angreal


@angreal.command(name="build", about="build your project for distribution")
def run_tests(integration=False, full=False, open=True):
    one_up = os.path.join(angreal.get_root(), "..")

    subprocess.run(
        (
        "python -m build --sdist --wheel --outdir dist/;"
        "pip install {{ package_name }} --no-index --find-links dist --force-reinstall"
        ), 
        shell=True, 
        cwd=one_up
    )
