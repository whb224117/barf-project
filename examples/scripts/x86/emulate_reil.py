#! /usr/bin/env python

from barf.barf import BARF

if __name__ == "__main__":
    #
    # Open file
    #
    barf = BARF("../../samples/bin/loop2.x86")

    #
    # REIL emulation
    #
    context_out = barf.emulate(start=0x080483ec, end=0x08048414)

    print "%s : %s" % ("eax", hex(context_out['registers']["eax"]))

    assert(context_out['registers']["eax"] == 0xa)
