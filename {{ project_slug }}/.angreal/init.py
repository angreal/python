import subprocess
import os

def init():
    import angreal
    from angreal.integrations.venv import VirtualEnv

    # Get the project directory (one level up from .angreal)
    project_dir = os.path.dirname(angreal.get_root())
    
    print("Initializing project...")
    
    # Set up git
    subprocess.run(["git", "config", "--global", "init.defaultBranch", "main"], cwd=project_dir, check=True)
    subprocess.run(["git", "init", "."], cwd=project_dir, check=True)
    subprocess.run(["git", "add", "."], cwd=project_dir, check=True)
    
    # Create and activate virtual environment
    print("Creating virtual environment...")
    venv_path = os.path.join(project_dir, ".venv")
    venv = VirtualEnv(venv_path)
    venv.create()
    venv.activate()
    
    # Install dependencies
    print("Installing dependencies...")
    venv.install(["-e", "..[dev]"])
    venv.install(["pre-commit"])
    
    # Set up pre-commit
    print("Setting up pre-commit...")
    subprocess.run([venv.python_executable, "-m", "pre_commit", "install"], cwd=project_dir, check=False) 
    subprocess.run([venv.python_executable, "-m", "pre_commit", "run", "--all-files"], cwd=project_dir, check=False)#first run actually cleans up
    
    # Commit changes
    print("Creating initial commit...")
    subprocess.run(["git", "commit", "-am", "test initialized via angreal"], cwd=project_dir, check=True)

    print("Initialization complete.")
