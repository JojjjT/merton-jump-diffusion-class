"""
Convierte todos los DOCX de docs/ a PDF usando LibreOffice.
Requiere LibreOffice instalado (busca soffice en PATH o en la instalación estándar de Windows).
"""
import os
import shutil
import subprocess
import tempfile

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF_DIR = os.path.join(BASE, "docs")

_candidates = [
    shutil.which("soffice"),
    r"C:\Program Files\LibreOffice\program\soffice.exe",
    r"C:\Program Files (x86)\LibreOffice\program\soffice.exe",
]
SOFFICE = next((c for c in _candidates if c and os.path.exists(c)), None)
if SOFFICE is None:
    raise SystemExit("No se encontró LibreOffice (soffice). Instálalo o agrégalo al PATH.")

def convertir(docx_path):
    outdir = os.path.dirname(docx_path)
    profile = os.path.join(tempfile.gettempdir(), "lo_profile_merton")
    os.makedirs(profile, exist_ok=True)
    cmd = [
        SOFFICE,
        "-env:UserInstallation=file:///" + profile.replace("\\", "/"),
        "--headless",
        "--convert-to",
        "pdf",
        "--outdir",
        outdir,
        docx_path,
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return res.returncode, res.stdout.strip(), res.stderr.strip()

def main():
    docx_files = [f for f in os.listdir(PDF_DIR) if f.lower().endswith(".docx")]
    print(f"Convirtiendo {len(docx_files)} archivos DOCX a PDF...")
    for f in docx_files:
        path = os.path.join(PDF_DIR, f)
        code, out, err = convertir(path)
        pdf_name = f[:-5] + ".pdf"
        pdf_path = os.path.join(PDF_DIR, pdf_name)
        status = "OK" if os.path.exists(pdf_path) else "FALLO"
        print(f"  {status} -> {pdf_name}")
        if code != 0:
            print(f"    stderr: {err}")

if __name__ == "__main__":
    main()
