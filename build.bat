virtualenv env
env/Scripts/activate.bat
py -m pip install pyinstaller
py -m PyInstaller --noconfirm --onefile --windowed --name "Study" "study.py"