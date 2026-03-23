# 🧠 Universal Compiler

Universal Compiler is an experimental GUI tool that detects source code language (Python, C, C++, Java) and builds standalone executables automatically.

⚠️ **Note:** This is a prototype for testing and demonstration. Features are incomplete and still under development.

---

## 🚧 Project Status

### ✅ Currently Supported

- 🐍 Python → EXE (via PyInstaller)  
- ⚙️ C / C++ → EXE (via GCC / MinGW)  
- ☕ Java → JAR → EXE (via Launch4j)  
- 🔍 Automatic language detection  
- 🖥️ GUI with file selector  
- 🚀 Splash screen  
- ⚙️ Config-based compiler rules  

---

## 🏗️ Running in Development

### 📦 Install Dependencies
```bash
pip install pyinstaller
pip install pillow

```
### ▶️Run the GUI
python gui.py
🛠️ Build Standalone EXE
pyinstaller universal_compiler.spec

### 📂 Output Location
dist/UniversalCompiler/

---
## 🧠 How It Works
- detector.py → Detects language using file extension
- loader.py → Loads compilers.json safely inside EXE
- builder.py → Executes compiler commands using subprocess
- gui.py → Handles GUI and background build process
- universal_compiler.spec → Manages EXE packaging, splash, icon
  
---
💡 Future Improvements
🌐 Add more languages (Go, Rust)
🧠 Smarter language detection
📝 Code editor with syntax highlighting
⚠️ Better error handling & debugging
📜 License

MIT License © 2025 Rituranjan Kumar

⚠️ Disclaimer

This project is a prototype. Use it only for testing or demonstration purposes. Not production-ready.


---
