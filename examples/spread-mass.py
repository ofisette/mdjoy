#!/usr/bin/env python3

from mdjoy import top

itp = top.read("protein-chain.itp")
atoms = [inst for inst in itp if isinstance(inst, top.GmxTopAtom)]

heavy_atom = None
for atom in atoms:
    if atom.atom.startswith("H"):
        atom.mass += 2.0
        heavy_atom.mass -= 2.0
    else:
        heavy_atom = atom

top.write(itp, "test.itp")
