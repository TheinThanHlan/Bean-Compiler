from .java import  Generator as java
from .ts import Generator as ts

generators=[java,ts]

def generate(tokens):
    for a in generators:
        a.generate(tokens)
