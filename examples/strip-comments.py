#!/usr/bin/env python3

from mdjoy import top

itp = top.read("protein-chain.itp")
atoms = [inst for inst in itp if isinstance(inst, top.GmxTopAtom)]

for atom in atoms:
    atom.comment = ""

top.write(itp, "test.itp")
