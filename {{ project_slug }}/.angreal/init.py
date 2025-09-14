import subprocess

def init():
    import os
    import angreal
    
    # Get the project directory (one level up from .angreal)
    project_dir = os.path.dirname(angreal.get_root())
    
    subprocess.run(
        (
            "git config --global init.defaultBranch main;"
            "git init .;"
            "git add .;"
            "pip install uv;"
            "uv venv;"
            ". .venv/bin/activate;"
            "uv pip install -e .[dev];"
            "pre-commit install;"
            "pre-commit run --all-files;"
            "git commit -am '{{ project_slug }} initialized via angreal';"
        ),
        shell=True,
        cwd=project_dir
    )

    print("Initialization complete.")
    pass
