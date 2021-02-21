import re

# just comment line
COMMENT_REGEX = "^\s*(//.*$)?$"
# label declaration
LABEL_REGEX = r'^\s*\(\s*(?P<label>[a-zA-Z_.$:][\w.$:]*)\s*\)\s*(//.*)?$'
# A-instruction
A_INSTRUCTION = "^\s*@\s*([a-zA-Z_.$:][\w.$:]|\d+)\s*(//.*$)?$"
# C-instruction
C_INSTRUCTION = ""
# todo finish this regex
