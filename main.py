from generator import Generator
import os

INPUT_DIR="input/"
INPUT_FILES=os.listdir(INPUT_DIR)


for a in INPUT_FILES:
    with open(INPUT_DIR+a,"r") as f:
        Generator.generate(eval(f.read()))


