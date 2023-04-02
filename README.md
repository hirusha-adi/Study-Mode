# Study-Mode

Run study related tasks easily with this script and zero basic programming knowledge

# Usage Guide

1. Create a file with the `.study` extension

```
browser google.com
notepad test.txt
run command
```

2. Run `study.py` or the compiled `study.exe`

- this script will open `google.com` in your default browser,
  then, open the `test.txt` file in notepad and then, run `command` in cmd

# Commands

1. ## browser

   - ### Usage

   ```
   browser <url>
   ```

   - ### Example

   ```
   browser google.com
   ```

2. ## notepad

   - ### Usage

   ```
   notepad <filePath>
   ```

   - ### Example

   ```
   notepad test.txt
   ```

3. ## run

   - ### Usage

   ```
   run <command>
   ```

   - ### Example

   ```
   run schtasks /create /tn "Alarm" /tr "powershell.exe -Command \"Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.MessageBox]::Show('Alarm!')\"" /sc once /st 08:00
   ```

# Build Guide

1. Install PyInstaller

```
py -m pip install pyinstaller
```

2. Compile

```
py -m PyInstaller --noconfirm --onefile --windowed --name "Study" "study.py"
```
