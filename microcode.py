from utilities import binary_to_hexadecimal

class Microcode:
    def __init__(self):
        self.microcode = list("00000000000000000000000000000000")
        self.bits = {
            "HLT": 0,
            "BRK": 1,
            "ALU_OP2": 13,
            "ALU_OP1": 14,
            "ALU_OP0": 15,
            "ALU_RE": 16,
            "OUT_WE": 17,
            "RB_RS": 18,
            "RB_RE": 19,
            "RB_WS": 20,
            "RB_WE": 21,
            "RAM_RE": 22,
            "RAM_WE": 23,
            "MAR_WE": 24,
            "IRIM_RE": 25,
            "IRIM_WE": 26,
            "IRIN_RE": 27,
            "IRIN_WE": 28,
            "PC_RE": 29,
            "PC_WE": 30,
            "PC_INC": 31
        }
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def __repr__(self):
        return binary_to_hexadecimal(''.join(self.microcode))
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def set_bit(self, bits):
        for bit in bits:
            self.microcode[self.bits[bit]] = '1'
###############################################################################
