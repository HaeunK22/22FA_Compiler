# -----------------------------------------------------------------------------
# SQLparser.py
#
#   expression : db DOT table DOT insert LPAREN LCURL term RCURL RPAREN
#
#   term : key COLON value
#        | term COMMA term
#
#   key : CHARACTER
#
#   db : CHARACTER
#
#   table : CHARACTER
#
#   insert : CHARACTER
#
#   value : QUOTE CHARACTER QUOTE
#         | INTEGER
#         | FLOAT
# ------------------------------------------------------------------------------

from ply.lex import lex
from ply.yacc import yacc

# --- Tokenizer

# All tokens must be named in advance.
tokens = ('CHARACTER', 'INTEGER', 'FLOAT', 'QUOTE', 'COLON', 'LCURL', 'RCURL', 'LPAREN', 'RPAREN', 'COMMA', 'DOT')

# Ignored characters
t_ignore = ' \t'

# Token matching rules are written as regexs
t_CHARACTER = r'[a-zA-Z_][a-zA-Z_]*'
t_INTEGER = r'\d+'
t_FLOAT = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
t_QUOTE = r'"'
# t_KEY = r'[a-zA-Z_][a-zA-Z_]*'
t_COLON = r'\:'
t_LCURL = r'\{'
t_RCURL = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r'\,'
# t_INSERT = r'\insert'
# t_DB = r'[a-zA-Z_][a-zA-Z_]*'
# t_TABLE = r'[a-zA-Z_][a-zA-Z_]*'
t_DOT = r'\.'

# A function can be used if there is an associated action.
# Write the matching regex in the docstring.

# Ignored token with an action associated with it
def t_ignore_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

# Error handler for illegal characters
def t_error(t):
    print(f'Illegal character {t.value[0]!r}')
    t.lexer.skip(1)

# Build the lexer object
lexer = lex()
lexer.input('db.products.insert({item:"card",qrt:15})')
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
    
# --- Parser

# Write functions for each grammar rule which is
# specified in the docstring.

db_name = []
table_name = []
item = {} # Item to add in table. key : value

def p_expression(p):
    '''
    expression : db DOT table DOT insert LPAREN LCURL term RCURL RPAREN
    '''
    print(p[2])
    # NEED FIX

def p_term(p):
    '''
    term : key COLON value
         | term COMMA term
    '''
    # NEED FIX

def p_key_char(p):
    '''
    key : CHARACTER
    '''
    p[0] = p[1]
    print(p[0])
    # NEED FIX
    
def p_db_char(p):
    '''
    db : CHARACTER
    '''
    p[0] = p[1]
    print(p[0])
    # NEED FIX

def p_table_char(p):
    '''
    table : CHARACTER
    '''
    p[0] = p[1]
    print(p[0])

    # NEED FIX
    
def p_insert_char(p):
    '''
    insert : CHARACTER
    '''
    p[0] = p[1]
    print(p[0])

    # NEED FIX
    
def p_value_string(p):
    '''
    value : QUOTE CHARACTER QUOTE
    '''
    p[0] = f"{p[1]}{p[2]}{p[3]}"
    print(p[0])
    # NEED FIX

def p_value_int(p):
    '''
    value : INTEGER
    '''
    p[0] = p[1]
    print(p[0])
    # NEED FIX

def p_value_char(p):
    '''
    value : FLOAT
    '''
    p[0] = p[1]
    print(p[0])
    # NEED FIX

def p_error(p):
    print(f'Syntax error at {p.value!r}')
    
# Build the parser
parser = yacc()

# Parse an expression
ast = parser.parse('db.products.insert({item:"card",qrt:15})')
print(ast)
