import conversion_tables as tables

# ===================
# Global Variables
# ===================
# the initial address that's allocated for new variable
INITIAL_ADDRESS = 16
# the prefix of an A-instruction in the .asm file
A_PREFIX = '@'
# equator char
EQUATION = '='
# semicolon char
SEMICOLON = ';'
# the binary prefix of the C-instruction
BINARY_C_PREFIX = '1'


def second_pass(lines_array, symbol_table):
    """
    iterates over the lines- which are A-instruction or C-instruction- checks whether the instruction syntax is valid,
    and returns an array of the appropriate binary codes.
    :param lines_array: the array of lines which are A instructions or C instructions only.
    :param symbol_table: the symbols table containing the pre-defined symbols and the label symbols.
    :return: binary_lines- the array of the commands in binary code
    """
    address = INITIAL_ADDRESS
    binary_lines = []
    for line in lines_array:
        if line.startswith(A_PREFIX):
            value, address = a_inst_parser(line, symbol_table, address)
            binary_lines.append(value)
        else:
            binary_lines.append(c_inst_parser(line))
    return binary_lines


def a_inst_parser(line, symbol_table, address):
    """ro
    checks validity of an A-instruction line- returns the apppriate binary code of the instruction.
    :param line: the A-instruction line to parse
    :param symbol_table: the current symbol table
    :param address: the address to allocate in case of a new variable
    :return: the binary code of the valided A instruction
    """
    line = line.strip(A_PREFIX)
    symbol_int = 0
    if line.isdigit():
        if line.startswith('-'):
            raise ValueError("Error: negative value in A-instruction")
        else:
            symbol_int = int(line)
    else:
        if line not in symbol_table.keys():
            symbol_table[line] = address
            address += 1
            symbol_int = symbol_table[line]
        else:
            symbol_int = symbol_table[line]

    return '{0:016b}'.format(symbol_int), address


def c_inst_parser(line):
    """
    checks validity of a C-instruction line- returns the appropriate binary code of the instruction.
    :param line: the C-instruction line to parse
    :return: the binary code of the validated C instruction
    """
    destination, comp, jump = 'null', 'null', 'null'
    if line.find(EQUATION) != -1:
        destination, comp_jump = line.split(EQUATION)[0], line.split(EQUATION)[1]
        if line.find(SEMICOLON) != -1:
            comp, jump = comp_jump.split(SEMICOLON)[0], comp_jump.split(SEMICOLON)[1]
        else:
            comp = comp_jump
    elif line.find(SEMICOLON) != -1:
        comp, jump = line.split(SEMICOLON)
    jump_code, comp_code, destination_code = jump_validity_check(jump), comp_validity_check(comp), \
                                             destination_validity_check(destination)
    if all([jump_code, comp_code, destination_code]):
        return BINARY_C_PREFIX + comp_code + destination_code + jump_code
    else:
        raise SyntaxError("Error: wrong C-instruction format.\nCode line is : '" + line + "'")


def jump_validity_check(jump_symbol):
    """
    validates the jump part of a C-instruction line
    :param jump_symbol: the jump symbol as appears in the line
    :return: The correct binary code if jump symbol is recognized, None otherwise
    """
    if jump_symbol in tables.jump_table.keys():
        return tables.jump_table[jump_symbol]
    return None


def comp_validity_check(comp_symbol):
    """
    validates the comp part of a C-instruction line
    :param comp_symbol: the comp symbol as appears in the line
    :return: The correct binary code if comp symbol is recognized, None otherwise
    """
    if comp_symbol in tables.comp_table.keys():
        return tables.comp_table[comp_symbol]
    return None


def destination_validity_check(dest_symbol):
    """
    validates the dest part of a C-instruction line
    :param dest_symbol:  the dest symbol as appears in the line
    :return: The correct binary code if dest symbol is recognized, None otherwise
    """
    if dest_symbol in tables.dest_table.keys():
        return tables.dest_table[dest_symbol]
    return None


if __name__ == '__main__':
    _line = '15'
    print('{0:016b}'.format(int(_line)))
    _line = '117'
    print('{0:016b}'.format(int(_line)))
