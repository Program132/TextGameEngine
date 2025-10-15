# TextGameEngine

**TextGameEngine** is a Python terminal-based game engine designed for ASCII graphics, UI elements, animations, sounds, and keyboard/mouse input. It allows you to create interactive games directly in the terminal.

---

## Features

- Terminal-based ASCII rendering.
- Interactive UI elements: buttons, menus, text.
- Supports animations and sounds.
- Mouse and keyboard input tracking.
- Adaptable to any terminal size.
- Examples included for learning and testing.

---

## Requirements

- Python 3.13+
- Virtual environment recommended.
- Install dependencies:

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Dependencies include:

- `PyAutoGUI`
- `pyfiglet`
- `pynput`
- `simpleaudio`
- `pyinstaller`
- `PyScreeze`, `PyRect`, `PyMsgBox`, `PyGetWindow`, `altgraph`, `evdev`, etc.

---

## Running the Engine

Activate your virtual environment:

```bash
source env/bin/activate
python main.py
```

---

## Compiling a Standalone Executable (Linux)

To package the engine as a single binary using PyInstaller:

1. **Clean previous builds**:

```bash
rm -rf build dist main.spec
```

2. **Create a PyInstaller hook for pyfiglet fonts**:

```bash
mkdir -p hooks
nano hooks/hook-pyfiglet.py
```

Paste the following:

```python
from PyInstaller.utils.hooks import collect_data_files
datas = collect_data_files('pyfiglet', includes=['fonts/*'])
```

This ensures the pyfiglet fonts are included in the binary.

3. **Build the executable**:

```bash
pyinstaller --onefile main.py --clean --additional-hooks-dir=hooks -v
```

Flags:

- `--onefile` → generate a single executable in `dist/`.
- `--clean` → clears PyInstaller cache.
- `--additional-hooks-dir` → include pyfiglet fonts.
- `-v` → verbose mode for debugging.

4. **Run the executable**:

```bash
cd dist
./main
```

---

## Examples

The `examples/` folder contains small scripts demonstrating engine features:

- Drawing shapes
- Handling events
- UI and menus
- Animations and sounds
- Multi-level games

---

## Notes

- The engine dynamically adapts to terminal size.
- Recommended terminal size for best experience: **236x61**
- Virtual environment is recommended for running and developing.
- All builds, caches, and environment folders are excluded via `.gitignore`.

---
