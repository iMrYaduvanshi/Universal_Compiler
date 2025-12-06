import os
import subprocess
import shutil


def run_command(cmd_list):
    """Run system commands safely."""
    result = subprocess.run(
        cmd_list,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    if result.returncode != 0:
        raise Exception(result.stderr.strip() or "Unknown compiler error")
    return result.stdout.strip()


def build_executable(source_file, lang, config):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    dist_dir = os.path.join(base_dir, "dist")
    build_dir = os.path.join(base_dir, "build")

    os.makedirs(dist_dir, exist_ok=True)
    os.makedirs(build_dir, exist_ok=True)

    file_name = os.path.splitext(os.path.basename(source_file))[0]
    output_exe = os.path.join(dist_dir, f"{file_name}.exe")
    output_jar = os.path.join(dist_dir, f"{file_name}.jar")

    if lang not in config:
        raise Exception(f"No compiler configuration found for: {lang}")

    compiler = config[lang].get("compiler")

    # ---------- PYTHON ----------
    if lang == "python":
        cmd = [
            compiler,
            "--onefile",
            "--distpath", dist_dir,
            "--workpath", build_dir,
            "--specpath", build_dir,
            source_file
        ]
        run_command(cmd)
        return output_exe

    # ---------- C ----------
    if lang == "c":
        cmd = [
            compiler,
            source_file,
            "-o", output_exe
        ]
        run_command(cmd)
        return output_exe

    # ---------- C++ ----------
    if lang == "cpp":
        cmd = [
            compiler,
            source_file,
            "-o", output_exe
        ]
        run_command(cmd)
        return output_exe

    # ---------- JAVA ----------
    if lang == "java":
        javac = compiler
        jar_tool = config[lang].get("jar")

        # 1. Compile
        run_command([javac, source_file])

        # 2. Manifest
        manifest = os.path.join(build_dir, "MANIFEST.MF")
        with open(manifest, "w") as mf:
            mf.write(f"Main-Class: {file_name}\n")

        # 3. JAR
        class_file = f"{file_name}.class"
        run_command([jar_tool, "cfm", output_jar, manifest, class_file])

        if os.path.exists(class_file):
            os.remove(class_file)

        return output_jar

    return "Unknown language"
