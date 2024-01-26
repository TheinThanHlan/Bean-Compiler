from .java import  Generator as java
from .cs import  Generator as cs
from .ts import Generator as ts

generators=[java,ts,cs]

def generate(tokens):
    for a in generators:
        a.generate(tokens)
