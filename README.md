# 🛠️ Universal Compiler (Work In Progress)

Universal Compiler is an experimental GUI tool that detects source code language (Python, C, C++, Java) and builds standalone executables.

⚠️ Note: This is a prototype for testing and demonstration. Features are incomplete and still under development.

## 🚧 Project Status

Currently supported:

✔ Python → EXE (via PyInstaller)

✔ C / C++ → EXE (via GCC/MinGW)

✔ Java → JAR → EXE (via Launch4j)

✔ Automatic language detection

✔ GUI with file selector

✔ Splash screen

✔ Config-based compiler rules

## 📂 Project Structure
Universal-Compiler/
│
├── gui.py
├── builder.py
├── detector.py
├── loader.py
├── universal_compiler.spec
│
├── config/
│   └── compilers.json
├── assets/
│   ├── icon.ico
│   └── splash.png
├── dist/               # generated executables/jars (ignored in git)
├── build/              # temporary PyInstaller files (ignored)
├── LICENSE
└── .gitignore

## 🏗 Running in Development

### Install dependencies:

pip install pyinstaller
pip install pillow


### Run the GUI:

python gui.py

### 🛠 Building the Standalone EXE
pyinstaller universal_compiler.spec


### Output will appear in:

dist/UniversalCompiler/

## 🧠 How It Works

detector.py → Detects language by file extension.

loader.py → Loads compilers.json safely inside EXE.

builder.py → Runs compiler commands using subprocess.

gui.py → Provides the user interface and background build thread.

universal_compiler.spec → Handles splash screen, icon, and EXE packaging.

# 📌 License

MIT License © 2025 RITURANJAN KUMAR

### ⚠ Disclaimer

This project is a prototype. Use it only for testing or demonstration. Not production-ready.
