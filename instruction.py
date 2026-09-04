from microcode import Microcode

class Instruction:
    def __init__(self, info):
        self.symbol = info[0]
        self.opcode = info[1]
        self.microcodes = [Microcode() for index in range(0, 8)]
        for index in range(0, 8):
            self.microcodes[index].set_bit(info[index + 2])
###############################################################################
