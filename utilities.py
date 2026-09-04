def binary_to_hexadecimal(binary, is_positive = True):
    while len(binary) % 4 != 0:
        binary = ('0' if is_positive else '1') + binary
    hexadecimal = ""
    for index in range(0, len(binary), 4):
        nibble = binary[index:index + 4]
        if nibble == "0000":
            hexadecimal += '0'
        elif nibble == "0001":
            hexadecimal += '1'
        elif nibble == "0010":
            hexadecimal += '2'
        elif nibble == "0011":
            hexadecimal += '3'
        elif nibble == "0100":
            hexadecimal += '4'
        elif nibble == "0101":
            hexadecimal += '5'
        elif nibble == "0110":
            hexadecimal += '6'
        elif nibble == "0111":
            hexadecimal += '7'
        elif nibble == "1000":
            hexadecimal += '8'
        elif nibble == "1001":
            hexadecimal += '9'
        elif nibble == "1010":
            hexadecimal += 'A'
        elif nibble == "1011":
            hexadecimal += 'B'
        elif nibble == "1100":
            hexadecimal += 'C'
        elif nibble == "1101":
            hexadecimal += 'D'
        elif nibble == "1110":
            hexadecimal += 'E'
        else:
            hexadecimal += 'F'
    return hexadecimal
###############################################################################
def integer_to_hexadecimal(integer, minimum_number_of_digits = 1):
    is_positive = True
    if integer < 0:
        is_positive = False
        integer *= -1
    binary = []
    while True:
        binary.insert(0, '1' if integer % 2 == 1 else '0')
        integer = int(integer / 2)
        if integer == 0:
            break
    if not is_positive:
        end = len(binary) - 1
        while binary[end] == '0':
            end -= 1
        for index in range(0, end):
            binary[index] = '1' if binary[index] == '0' else '0'
    hexadecimal = binary_to_hexadecimal(''.join(binary), is_positive)
    while len(hexadecimal) < minimum_number_of_digits:
        hexadecimal = ('0' if is_positive else 'F') + hexadecimal
    return hexadecimal
###############################################################################
