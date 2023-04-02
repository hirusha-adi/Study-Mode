import os
import webbrowser


def _browser(value: str):
    webbrowser.open(value)


def _notepad(value: list):
    os.system(f"notepad {value}")


def _run(value: str):
    os.system(value)


def parse_commands(content: str):
    for line in content.splitlines():
        if line.startswith("browser"):
            _browser(' '.join(line.split()[1:]))
        elif line.startswith("notepad"):
            _notepad(' '.join(line.split()[1:]))
        elif line.startswith("run"):
            _run(' '.join(line.split()[1:]))


cwd = os.getcwd()
for name in os.listdir(os.getcwd()):
    if name.endswith(".study"):
        with open(os.path.join(os.getcwd(), name), 'r', encoding='utf-8') as file:
            parse_commands(content=file.read())
