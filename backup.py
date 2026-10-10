'''import subprocess
from pathlib import Path

base = Path(__file__).resolve().parent
env = (base / ".env").read_text().splitlines()
key = next(
    line.split("=", 1)[1].strip().strip("'\"")
    for line in env
    if line.startswith("KEY=")
)

subprocess.run(
    [
        r"C:\Program Files\7-Zip\7z.exe",
        "a",
        "-tzip",
        str(base / "music.zip"),
        str(base / "music"),
        f"-p{key}",
        "-mem=AES256",
        "-y",
    ],
    check=True,
)'''

import subprocess
from pathlib import Path

base = Path(__file__).resolve().parent
env = (base / ".env").read_text().splitlines()
key = next(
    line.split("=", 1)[1].strip().strip("'\"")
    for line in env
    if line.startswith("KEY=")
)

subprocess.run(
    [
        r"C:\Program Files\7-Zip\7z.exe",
        "a",
        "-tzip",
        str(base / "music.zip"),
        str(base / "music"),
        f"-p{key}",
        "-mem=AES256",
        "-v99m",  # Splits the archive into chunks of 99 MB max
        "-y",
    ],
    check=True,
)