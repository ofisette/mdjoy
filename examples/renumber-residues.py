#!/usr/bin/env python3

from mdjoy import top

itp = top.read("protein-chain.itp")
atoms = [inst for inst in itp if isinstance(inst, top.GmxTopAtom)]

n = 23
prev_resnr = atoms[0].resnr
for atom in atoms:
    if atom.resnr != prev_resnr:
        prev_resnr = atom.resnr
        n += 1
    atom.resnr = n

top.write(itp, "test.itp")
