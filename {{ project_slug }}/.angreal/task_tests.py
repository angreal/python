import angreal
from angreal.integrations.venv import VirtualEnv

import os
import subprocess
import webbrowser

cwd = os.path.join(angreal.get_root(),'..')
test = angreal.command_group(name="test", about="commands for testing the application and library")


@test()
@angreal.command(name="unit", about="run unit tests")
@angreal.argument(name="open", long="open", short='o', 
                  takes_value=False, help="open results in web browser")
def unit_tests(open=False):
    venv_path = os.path.join(cwd, '.venv')
    output_file = os.path.realpath(os.path.join(cwd,'htmlcov','index.html'))
    
    with VirtualEnv(path=venv_path, now=True) as venv:
        # Install test dependencies
        print("Installing test dependencies...")
        venv.install(["pytest", "pytest-cov"])
        
        # Run unit tests using venv's python
        print("Running unit tests...")
        subprocess.run([
            venv.python_executable, '-m', 'pytest', '-vvv',
            '--cov=src/{{ package_name }}', '--cov-report', 'html', '--cov-report', 'term',
            'tests/unit'
        ], cwd=cwd)
        
        if open:
            webbrowser.open_new('file://{}'.format(output_file))


@test()
@angreal.command(name="integration", about="run integration tests")
@angreal.argument(name="open", long="open", short='o', 
                  takes_value=False, help="open results in web browser")
def integration_tests(open=False):
    venv_path = os.path.join(cwd, '.venv')
    output_file = os.path.realpath(os.path.join(cwd,'htmlcov','index.html'))
    
    with VirtualEnv(path=venv_path, now=True) as venv:
        # Install test dependencies
        print("Installing test dependencies...")
        venv.install(["pytest", "pytest-cov"])
        
        # Run integration tests using venv's python
        print("Running integration tests...")
        subprocess.run([
            venv.python_executable, '-m', 'pytest', '-vvv',
            '--cov=src/{{ package_name }}', '--cov-report', 'html', '--cov-report', 'term',
            'tests/integration'
        ], cwd=cwd)
        
        if open:
            webbrowser.open_new('file://{}'.format(output_file))

@test()
@angreal.command(name="all", about="run all tests (unit and integration)")
@angreal.argument(name="open", long="open", short='o', 
                  takes_value=False, help="open results in web browser")
def all_tests(open=False):
    venv_path = os.path.join(cwd, '.venv')
    output_file = os.path.realpath(os.path.join(cwd,'htmlcov','index.html'))
    
    with VirtualEnv(path=venv_path, now=True) as venv:
        # Install test dependencies
        print("Installing test dependencies...")
        venv.install(["pytest", "pytest-cov"])
        
        # Run all tests using venv's python
        print("Running all tests...")
        subprocess.run([
            venv.python_executable, '-m', 'pytest', '-vvv',
            '--cov=src/{{ package_name }}', '--cov-report', 'html', '--cov-report', 'term',
            'tests/'
        ], cwd=cwd)
        
        if open:
            webbrowser.open_new('file://{}'.format(output_file))

@test()
@angreal.command(name='static', about="run our static analysis")
@angreal.argument(name="open", long="open", short='o',
                   takes_value=False, help="open results in web browser")
def setup_env(open):
    venv_path = os.path.join(cwd, '.venv')
    
    with VirtualEnv(path=venv_path, now=True) as venv:
        # Install static analysis dependencies
        print("Installing static analysis dependencies...")
        venv.install(["mypy"])
        
        # Run mypy using venv's python
        print("Running static analysis...")
        subprocess.run([
            venv.python_executable, '-m', 'mypy', 'src/{{package_name}}',
            '--ignore-missing-imports', '--html-report', 'typing_report'
        ], cwd=cwd)

        if open:
            webbrowser.open(f'file:://{os.path.join(cwd,"typing_report","index.html")}')
