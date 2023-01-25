import subprocess

def init():
    subprocess.run(
        (
            "git init .;"
            "git add .;"
            "mkdir -p .venv/angreal_python_dev;"
            "python3 -m venv .venv/angreal_python_dev;"
            "pip install -e .[dev];"
            "pre-commit install;"
            "pre-commit run --all-files;"
            "git commit -am '{{ project_slug }} initialized via angreal';"
            "git branch -m master main;"
        ),
        shell=True,
        cwd="{{ project_slug }}"
    )

    print("Initialization complete.")
    print("You'll need to run 'git remote add origin git@github.com:{{ github_username }}/{{ project_slug }}.git'")
    pass