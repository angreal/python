import angreal

import os
import subprocess
import webbrowser



@angreal.command(name='static-analysis', about="run our static analysis")
@angreal.argument(name="open", long="open", short='o', takes_value=False, help="open results in web browser")
def setup_env(open):
    one_up = os.path.join(angreal.get_root(), '..')    
    subprocess.run(
        (
            "mypy {{package_name}} --ignore-missing-imports --html-report typing_report"
        ),
        shell=True,
        cwd=one_up
    )

    if open:
        webbrowser.open(f'file:://{os.path.join(one_up,"typing_report","index.html")}')
