import pathlib
import os
from icecream import ic

config = list()
with open("pyproject copy.toml", "r") as f:
    for line in f.readlines():
        config.append(line.strip(f"{str(0xff)}"))

print(config)
for character in config[0]:
    ic(ord(character), str(character))
pathlib.Path("pyproject.toml").unlink(missing_ok=True)
with open("pyproject.toml", "x") as f:
    for line in config:
        f.write(line)
