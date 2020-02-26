#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

LDI = 0b10000010
PRN = 0b01000111
HLT = 0b00000001
MUL = 0b10100010

cpu = CPU()

cpu.load(sys.argv[1])
cpu.run()
