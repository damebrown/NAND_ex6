import re

import regex_patterns as rp

NUM_OF_REGISTERS = 16


def generate_predefined_symbol_table():
    """
    generates a dictionary of the predefined symbols in hack language as
    described in the language specification
    :return: a dictionary of the predefined symbols in hack language
    """
    table = {'SCREEN': 16384, 'KBD': 24576, 'SP': 0, 'LCL': 1, 'ARG': 2,
             'THIS': 3, 'THAT': 4}
    for i in range(NUM_OF_REGISTERS):
        table['R' + str(i)] = i
    return table


def first_pass(lines):
    """
    performs a first pass on a code file represented by lines.
    1) cleans:
        - white space
        - comments
        - label declaration lines
    2) generates a symbol list of predefined symbols and labels declared in the
       code
    :param lines: an array of string representing the raw data of a code file
    :return: tuple (clean_code, symbol_table) where:
                clean_code: the code after removing white space and comments
                symbol_table: a list of symbols including predefined and labels
                              declared in the code
    :raises ValueError: if the code has bad syntax, message will have the line
    number and line content
    """
    clean_lines = []
    symbol_table = generate_predefined_symbol_table()
    for index, line in enumerate(lines):
        if re.match(rp.COMMENT_REGEX, line):
            continue
        label_line_match = re.match(rp.LABEL_REGEX, line)
        if label_line_match:
            label = label_line_match.group('label')
            symbol_table[label] = len(clean_lines)
            continue
        line = line.split("//")[0].strip().replace(" ", "")
        clean_lines.append(line)
    return clean_lines, symbol_table
