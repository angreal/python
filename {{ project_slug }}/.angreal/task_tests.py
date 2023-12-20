import angreal
from angreal.integrations.venv import venv_required

import os
import subprocess
import webbrowser

venv_path = os.path.join(angreal.get_root(),'..','.venv')
cwd = os.path.join(angreal.get_root(),'..')
test = angreal.command_group(name="test", about="commands for testing the"
                             " application and library")


@test()
@angreal.command(name="unit", about="run unit tests")
@angreal.argument(name="open", long="open", short='o', 
                  takes_value=False, help="open results in web browser")
@venv_required(venv_path)
def unit_tests(open=False):
    output_file = os.path.realpath(os.path.join(cwd,'htmlcov','index.html'))
    subprocess.run('pytest -vvv --cov={{ package_name }} '
                   '--cov-report html --cov-report term tests/unit',shell=True, cwd=cwd)    
    if open:
        webbrowser.open_new('file://{}'.format(output_file))


@test()
@angreal.command(name="integration", about="run integration tests")
@angreal.argument(name="open", long="open", short='o', 
                  takes_value=False, help="open results in web browser")
@venv_required(venv_path)
def integration_tests(open=False):
    output_file = os.path.realpath(os.path.join(cwd,'htmlcov','index.html'))
    subprocess.run('pytest -vvv --cov={{ package_name }} --cov-report html'
                   ' --cov-report term tests/integration',shell=True, cwd=cwd)
    if open:
        webbrowser.open_new('file://{}'.format(output_file))

@test()
@angreal.command(name='static', about="run our static analysis")
@angreal.argument(name="open", long="open", short='o',
                   takes_value=False, help="open results in web browser")
@venv_required(venv_path)
def setup_env(open):

    subprocess.run(
        (
            "mypy {{package_name}} --ignore-missing-imports --html-report typing_report"
        ),
        shell=True,
        cwd=cwd
    )

    if open:
        webbrowser.open(f'file:://{os.path.join(cwd,"typing_report","index.html")}')
