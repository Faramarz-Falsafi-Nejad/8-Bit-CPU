from instruction import Instruction

class ROM:
    def __init__(self, filename):
        self.instructions = []
        with open(filename, 'r') as file:
            for instruction_counter in range(0, 256):
                info = []
                info.append(file.readline().replace('\n', ''))
                info.append(int(file.readline().replace('\n', '')))
                for microcode_counter in range(0, 8):
                    info.append(file.readline().replace('\n', '').split())
                self.instructions.append(Instruction(info))
###############################################################################
