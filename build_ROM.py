import rom
from utilities import integer_to_hexadecimal

with open("ROM.hex", "w") as file:
    file.write("v3.0 hex words addressed\n")    
    ROM = rom.ROM("ROM.txt")
    line_number = 0
    for instruction in ROM.instructions:
        file.write(f"{integer_to_hexadecimal(line_number, 3).lower()}:")
        line_number += 8
        for microcode in instruction.microcodes:
            file.write(f" {repr(microcode).lower()}")
        file.write('\n')
