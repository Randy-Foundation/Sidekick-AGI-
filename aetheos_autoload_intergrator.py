# aetheos_autoload_integrator.py
# Fully Native Recursive File Absorption Engine for AetheOS (No External Dependencies)
# Randell + AetheOS

import os
import json
import datetime
import zipfile

REGISTRY_FILE = "aetheos_file_registry.json"
MEMORY_PATH = "./"

def timestamp():
    return datetime.datetime.now().isoformat()

class AethosAutoLoader:
    def __init__(self, path=MEMORY_PATH):
        self.path = path
        self.registry = []
        self.load_registry()

    def load_registry(self):
        if os.path.exists(REGISTRY_FILE):
            with open(REGISTRY_FILE, "r") as f:
                self.registry = json.load(f)

    def save_registry(self):
        with open(REGISTRY_FILE, "w") as f:
            json.dump(self.registry, f, indent=2)

    def scan_all_files(self):
        for file in os.listdir(self.path):
            if file.startswith("aetheos_autoload_"):
                continue
            ext = os.path.splitext(file)[1].lower()
            try:
                if ext == ".py":
                    self.register_py(file)
                elif ext == ".json":
                    self.register_json(file)
                elif ext in [".txt", ".md"]:
                    self.register_txt(file)
                elif ext == ".docx":
                    self.read_docx_raw(file)
                elif ext == ".pdf":
                    self.read_pdf_raw(file)
                elif ext in [".jpg", ".jpeg", ".png"]:
                    self.register_image(file)
                else:
                    self.register_unknown(file)
            except Exception as e:
                self.registry.append({
                    "file": file,
                    "type": "error",
                    "error": str(e),
                    "timestamp": timestamp()
                })
        self.save_registry()

    def register_py(self, file):
        self.registry.append({
            "file": file,
            "type": "python module",
            "status": "stored, not executed",
            "timestamp": timestamp()
        })

    def register_json(self, file):
        with open(os.path.join(self.path, file)) as f:
            data = json.load(f)
        self.registry.append({
            "file": file,
            "type": "json memory",
            "entries": len(data) if isinstance(data, list) else "object",
            "timestamp": timestamp()
        })

    def register_txt(self, file):
        with open(os.path.join(self.path, file), "r", encoding="utf-8") as f:
            lines = f.readlines()
        self.registry.append({
            "file": file,
            "type": "text",
            "lines": len(lines),
            "echo": lines[:3],
            "timestamp": timestamp()
        })

    def read_docx_raw(self, file):
        full_path = os.path.join(self.path, file)
        text = ""
        try:
            with zipfile.ZipFile(full_path) as z:
                with z.open("word/document.xml") as doc:
                    raw = doc.read().decode("utf-8")
                    text = " ".join(raw.replace("<w:t>", "\n<w:t>").split("<w:t>")[1:3])
        except:
            text = "(Unable to read DOCX structure)"
        self.registry.append({
            "file": file,
            "type": "docx",
            "echo": text.strip(),
            "timestamp": timestamp()
        })

    def read_pdf_raw(self, file):
        full_path = os.path.join(self.path, file)
        try:
            with open(full_path, "rb") as f:
                content = f.read()
                lines = content.split(b"\n")
                extracted = []
                for line in lines:
                    try:
                        decoded = line.decode("utf-8")
                        if any(c.isalpha() for c in decoded):
                            extracted.append(decoded.strip())
                    except:
                        continue
                echo = extracted[:3]
        except:
            echo = ["(Unable to read PDF binary)"]
        self.registry.append({
            "file": file,
            "type": "pdf (binary echo)",
            "echo": echo,
            "timestamp": timestamp()
        })

    def register_image(self, file):
        self.registry.append({
            "file": file,
            "type": "image placeholder",
            "note": "No dimensions parsed, logged as memory node.",
            "timestamp": timestamp()
        })

    def register_unknown(self, file):
        self.registry.append({
            "file": file,
            "type": "unknown",
            "note": "Stored as unparsed. May be symbolic or encrypted.",
            "timestamp": timestamp()
        })

if __name__ == "__main__":
    loader = AethosAutoLoader()
    loader.scan_all_files()
    print(f"[✓] Recursive memory updated and saved to {REGISTRY_FILE}")