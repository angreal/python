import subprocess

def init():
    subprocess.run(
        (
            "git init . --initial-branch=main;"
            "git add .;"
            "mkdir -p .venv/{{ project_slug }};"
            "python3 -m venv .venv/{{ project_slug }};"
            ". .venv/{{ project_slug }}/bin/activate;"
            "python3 -m pip install -e .[dev];"
            "pre-commit install;"
            "pre-commit run --all-files;"
            "git commit -am '{{ project_slug }} initialized via angreal';"
        ),
        shell=True,
        cwd="{{ project_slug }}"
    )

    print("Initialization complete.")
    print("You'll need to run 'git remote add origin git@github.com:{{ github_username }}/{{ project_slug }}.git'")
    pass