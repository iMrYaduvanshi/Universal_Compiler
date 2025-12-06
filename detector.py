import os

def detect_language(file_path):
    ext = file_path.lower().split(".")[-1]

    if ext == "py":
        return "python"
    if ext == "c":
        return "c"
    if ext in ["cpp", "cc", "cxx"]:
        return "cpp"
    if ext == "java":
        return "java"

    return None

