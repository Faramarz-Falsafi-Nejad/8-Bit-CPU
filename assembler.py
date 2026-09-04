from utilities import integer_to_hexadecimal

def NOP():
    return ["00"]
##############################################################################
def LDA(immediate):
    opcode = "01"
    if immediate.startswith("#$"):
        immediate = immediate[2:]
    elif immediate.startswith('#'):
        immediate = integer_to_hexadecimal(int(immediate[1:]), 2)
    else:
        opcode = "02"
        immediate = immediate[1:]
    return [opcode, immediate]
##############################################################################
def ADD(immediate):
    opcode = "0F"
    if immediate.startswith("#$"):
        immediate = immediate[2:]
    elif immediate.startswith('#'):
        immediate = integer_to_hexadecimal(int(immediate[1:]), 2)
    else:
        opcode = "03"
        immediate = immediate[1:]
    return [opcode, immediate]
##############################################################################
def SUB(immediate):
    opcode = "18"
    if immediate.startswith("#$"):
        immediate = immediate[2:]
    elif immediate.startswith('#'):
        immediate = integer_to_hexadecimal(int(immediate[1:]), 2)
    else:
        opcode = "04"
        immediate = immediate[1:]
    return [opcode, immediate]
##############################################################################
def STA(address):
    return ["05", address[1:]]
##############################################################################
def JMP(address):
    return ["06", address[1:]]
##############################################################################
def XOR(immediate):
    opcode = "07"
    if immediate.startswith("#$"):
        immediate = immediate[2:]
    elif immediate.startswith('#'):
        immediate = integer_to_hexadecimal(int(immediate[1:]), 2)
    else:
        opcode = "08"
        immediate = immediate[1:]
    return [opcode, immediate]
##############################################################################
def NOT():
    return ["09"]
##############################################################################
def OUT():
    return ["0A"]
##############################################################################
def AND(immediate):
    opcode = "0B"
    if immediate.startswith("#$"):
        immediate = immediate[2:]
    elif immediate.startswith('#'):
        immediate = integer_to_hexadecimal(int(immediate[1:]), 2)
    else:
        opcode = "0C"
        immediate = immediate[1:]
    return [opcode, immediate]
##############################################################################
def OR(immediate):
    opcode = "0D"
    if immediate.startswith("#$"):
        immediate = immediate[2:]
    elif immediate.startswith('#'):
        immediate = integer_to_hexadecimal(int(immediate[1:]), 2)
    else:
        opcode = "0E"
        immediate = immediate[1:]
    return [opcode, immediate]
##############################################################################
def SHR():
    return ["10"]
##############################################################################
def SHL():
    return ["11"]
##############################################################################
def BEQ(address):
    return ["12", address[1:]]
##############################################################################
def BNE(address):
    return ["13", address[1:]]
##############################################################################
def BPL(address):
    return ["14", address[1:]]
##############################################################################
def BMI(address):
    return ["15", address[1:]]
##############################################################################
def BCS(address):
    return ["16", address[1:]]
##############################################################################
def BCC(address):
    return ["17", address[1:]]
##############################################################################
def HLT():
    return ["FF"]
##############################################################################
def Assembler(source):
    code = []
    with open(source, 'r') as file:
        for line in file.readlines():
            if line.isspace() or line.startswith(';'):
                continue
            else:
                start = 0
                end = line.find(';')
                instruction = line[start:end]
                code += instruction.split()
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    labels = {}
    index = 0
    while index < len(code):
        if code[index].endswith(':'):
            labels.update({f"{code[index].replace(':', '')}": index})
            code.pop(index)
        else:
            index += 1
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    for index in range(0, len(code)):
        if code[index].replace(':', '') in labels.keys():
            code[index] = f"${integer_to_hexadecimal(labels[code[index]], 2)}"
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    executable = []
    index = 0
    while index < len(code):
        mnemonic = code[index]
        if mnemonic == "NOP":
            executable += NOP()
        elif mnemonic == "LDA":
            index += 1
            executable += LDA(code[index])
        elif mnemonic == "ADD":
            index += 1
            executable += ADD(code[index])
        elif mnemonic == "SUB":
            index += 1
            executable += SUB(code[index])
        elif mnemonic == "STA":
            index += 1
            executable += STA(code[index])
        elif mnemonic == "JMP":
            index += 1
            executable += JMP(code[index])
        elif mnemonic == "XOR":
            index += 1
            executable += XOR(code[index])
        elif mnemonic == "NOT":
            executable += NOT()
        elif mnemonic == "OUT":
            executable += OUT()
        elif mnemonic == "AND":
            index += 1
            executable += AND(code[index])
        elif mnemonic == "OR":
            index += 1
            executable += OR(code[index])
        elif mnemonic == "SHR":
            executable += SHR()
        elif mnemonic == "SHL":
            executable += SHL()
        elif mnemonic == "BEQ":
            index += 1
            executable += BEQ(code[index])
        elif mnemonic == "BNE":
            index += 1
            executable += BNE(code[index])
        elif mnemonic == "BPL":
            index += 1
            executable += BPL(code[index])
        elif mnemonic == "BMI":
            index += 1
            executable += BMI(code[index])
        elif mnemonic == "BCS":
            index += 1
            executable += BCS(code[index])
        elif mnemonic == "BCC":
            index += 1
            executable += BCC(code[index])
        elif mnemonic == "HLT":
            executable += HLT()
        else:
            pass
        index += 1
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    while len(executable) <= 256:
        executable += HLT()
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    return executable
##############################################################################

program = Assembler("Assembly/Countdown_Loop_with_SUB_Immediate.asm")

with open("Programs/Countdown_Loop_with_SUB_Immediate.hex", 'w') as output:
    output.write("v3.0 hex words addressed\n")
    for row in range(0, 256, 16):
        output.write(f"{integer_to_hexadecimal(row, 2).lower()}:")
        for index in range(row, row + 16):
            output.write(f" {program[index].lower()}")
        output.write('\n')
