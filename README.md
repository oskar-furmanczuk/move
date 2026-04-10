# Move - Activity Keeper

A lightweight Python script that prevents your workstation from going idle by simulating mouse movement and keyboard input when no user activity is detected.

## How It Works

The script monitors mouse position every 10–180 seconds (random interval). If no movement is detected for **60 seconds** and the current time falls within **working hours (07:02–22:02 Warsaw time)**, it will:

1. Move the mouse to a random nearby position (±150px)
2. Wait a random delay (5–30 seconds)
3. Press `Scroll Lock` twice to simulate keyboard activity
4. Reset the inactivity timer

## Requirements

- Python 3.9+
- `pyautogui` library

```bash
pip install pyautogui
```

## Usage

```bash
python mouse_keeper.py
```

The script runs in an infinite loop and logs all actions to the console. To stop it, press `Ctrl+C` in the terminal.

## Run at Windows Startup

To launch the script silently in the background on every login (no console window), use `pythonw`:

1. Press `Win + R`, type `shell:startup`, and press Enter — this opens the Startup folder
2. Create a new shortcut in that folder
3. Set the shortcut target to:

```
pythonw.exe C:\fullpath\tomouse_keeper.py
```

> **Tip:** Use the full path to `pythonw.exe` if it's not on your PATH, e.g.:
> `C:Users<YourUser>AppDataLocalProgramsPythonPython3xpythonw.exe`

The script will now start silently every time you log into Windows, with no console window visible.

## Configuration

| Parameter | Default | Description |
|---|---|---|
| Inactivity threshold | 60s | Time before triggering actions |
| Active hours | 07:02–22:02 | Warsaw time (Europe/Warsaw) |
| Check interval | 10–180s | Random delay between checks |
| Mouse movement range | ±150px | Max displacement per move |

## Notes

- `FAILSAFE` is disabled — the script won't abort if the mouse reaches a screen corner
- Requires display access; won't work in headless environments
