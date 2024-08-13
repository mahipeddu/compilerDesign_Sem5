import re

def zephy(code):
    keywords = ['int', 'float', 'char', 'if', 'else', 'for', 'while', 'do', 'return']
    vars = []

    keywords = r'\b(' + '|'.join(keywords) + r')\b'
    identifier_pat = r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'
    var_pat = r'\b(?:int|float|char)\s+([a-zA-Z_][a-zA-Z0-9_]*)'


    extracted_keywords = re.findall(keywords, code)
    vars = re.findall(var_pat, code)

    print('Keywords:', extracted_keywords)

    print('Variable Names:', vars)

i = input()

zephy(i)
