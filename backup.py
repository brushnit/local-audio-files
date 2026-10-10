import subprocess
from pathlib import Path

base = Path(__file__).resolve().parent
env = (base / ".env").read_text().splitlines()
key = next(
    line.split("=", 1)[1].strip().strip("'\"")
    for line in env
    if line.startswith("KEY=")
)

# Define and create the output directory
output_dir = Path("/data")
output_dir.mkdir(parents=True, exist_ok=True)

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