import os
import subprocess
import webbrowser

import angreal

one_up = os.path.join(angreal.get_root(), "..")


@angreal.command(name="build-docs", about="build our doc site")
@angreal.argument(name="open", long="open", short="o", takes_value=False, help="open results in web browser")
def run_tests(open=False):
    one_up = os.path.join(angreal.get_root(), "..","docs")
    
    subprocess.run(
        (
            "hugo"
        ),
        shell=True,
        cwd=one_up,
    )
    
    if open:
        subprocess.run(
            (
                "hugo serve&"
            ),
            shell=True,
            cwd=one_up,
        )   
        webbrowser.open_new("http://localhost:1313/{{ project_slug }}/")
