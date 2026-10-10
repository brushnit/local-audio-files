import subprocess
from pathlib import Path

base = Path(__file__).resolve().parent
env = (base / ".env").read_text().splitlines()
key = next(
    line.split("=", 1)[1].strip().strip("'\"")
    for line in env
    if line.startswith("KEY=")
)

# Define and create the local data directory inside your project folder
output_dir = base / "data"
output_dir.mkdir(parents=True, exist_ok=True)

# Completely clear out any old files in the data directory 
# so only the newest backup parts remain
for existing_file in output_dir.iterdir():
    if existing_file.is_file():
        existing_file.unlink()

# Run 7-Zip to create the new multi-volume archive
subprocess.run(
    [
        r"C:\Program Files\7-Zip\7z.exe",
        "a",
        "-tzip",
        str(output_dir / "music.zip"),
        str(base / "music"),
        f"-p{key}",
        "-mem=AES256",
        "-v99m",
        "-y",
    ],
    check=True,
)