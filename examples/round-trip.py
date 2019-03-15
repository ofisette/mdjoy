#!/usr/bin/env python3

from mdjoy import top

itp = top.read("protein-chain.itp")
top.write(itp, "test.itp")
