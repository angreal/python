import angreal
from angreal.integrations.venv import VirtualEnv

import os
import subprocess

cwd = os.path.join(angreal.get_root(),'..')

@angreal.command(name="lint", about="run linting, formatting, and type checking")
def lint():
    """Run Ruff for linting and formatting, then mypy for type checking."""
    venv_path = os.path.join(cwd, '.venv')
    
    with VirtualEnv(path=venv_path, now=True) as venv:
        print("Running Ruff linter with auto-fix...")
        result1 = subprocess.run('ruff check --fix .', shell=True, cwd=cwd)
        
        print("Running Ruff formatter...")
        result2 = subprocess.run('ruff format .', shell=True, cwd=cwd)
        
        print("Running mypy type checker...")
        result3 = subprocess.run('mypy src/{{ package_name }}', shell=True, cwd=cwd)
        
        # Return non-zero exit code if any command failed
        if result1.returncode != 0 or result2.returncode != 0 or result3.returncode != 0:
            return 1
        
        print("All linting, formatting, and type checking completed successfully!")
        return 0