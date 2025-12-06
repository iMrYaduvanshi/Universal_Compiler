# ------------------------------------
# Close PyInstaller splash screen
# ------------------------------------
try:
    import pyi_splash
    pyi_splash.close()   # MUST be first line
except:
    pass
# ------------------------------------

import tkinter as tk
from tkinter import filedialog, messagebox
import threading
from builder import build_executable
from detector import detect_language
from loader import load_config


class UniversalCompilerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Universal Compiler")
        self.root.geometry("620x420")
        self.file_path = None

        tk.Label(root, text="Universal Compiler",
                 font=("Arial", 20, "bold")).pack(pady=10)

        self.load_btn = tk.Button(
            root, text="Choose File to Compile", font=("Arial", 12),
            command=self.choose_file
        )
        self.load_btn.pack(pady=10)

        self.status = tk.Text(root, height=12, width=70, font=("Consolas", 10))
        self.status.pack(pady=10)

        self.build_btn = tk.Button(
            root, text="Build Executable", font=("Arial", 12),
            state="disabled", command=self.start_build_thread
        )
        self.build_btn.pack(pady=10)

    def log(self, text):
        self.status.insert(tk.END, text + "\n")
        self.status.see(tk.END)

    def choose_file(self):
        path = filedialog.askopenfilename()

        if not path:
            return

        self.file_path = path
        self.log(f"✔ File loaded: {path}")

        lang = detect_language(path)

        if not lang:
            messagebox.showerror("Error", "Could not detect language!")
            return

        self.log(f"✔ Language detected: {lang}")
        self.detected_lang = lang

        self.build_btn.configure(state="normal")

    def start_build_thread(self):
        thread = threading.Thread(target=self.run_build)
        thread.start()

    def run_build(self):
        self.log("\n⚙ Building... Please wait...")

        try:
            config = load_config()
            output_path = build_executable(
                self.file_path, self.detected_lang, config
            )
            self.log(f"\n✔ Build complete! Output: {output_path}")

        except Exception as e:
            self.log("\n❌ Error: " + str(e))
            messagebox.showerror("Build Failed", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = UniversalCompilerGUI(root)
    root.mainloop()
