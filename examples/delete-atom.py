#!/usr/bin/env python3

from mdjoy import top

itp = top.read("protein-chain.itp")
atoms = [inst for inst in itp if isinstance(inst, top.GmxTopAtom)]

for atom in atoms:
    if atom.resnr == 21:
        if atom.atom == "HD22":
            HD22 = atom
        elif atom.atom == "ND2":
            ND2 = atom

deleted_nr = HD22.nr
ND2.charge += HD22.charge
new_itp = []

for inst in itp:
    atom_nrs = inst.get_atom_nrs()
    if deleted_nr in atom_nrs:
        pass
    else:
        new_atom_nrs = []
        for nr in atom_nrs:
            if nr < deleted_nr:
                new_atom_nrs.append(nr)
            else:
                new_atom_nrs.append(nr - 1)
        inst.set_atom_nrs(new_atom_nrs)
        new_itp.append(inst)

top.write(new_itp, "test.itp")
