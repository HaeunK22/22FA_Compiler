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
#   value : QUOT CHARACTER QUOT
#         | INTEGER
#         | FLOAT
# ------------------------------------------------------------------------------

from ply.lex import lex
from ply.yacc import yacc

# --- Tokenizer

# All tokens must be named in advance.
tokens = ('CHARACTER', 'INTEGER', 'FLOAT', 'QUOT', 'COLON', 'LCURL', 'RCURL', 'LPAREN', 'RPAREN', 'COMMA', 'DOT')

# Ignored characters
t_ignore = ' \t'

# Token matching rules are written as regexs
t_CHARACTER = r'[a-zA-Z_][a-zA-Z_]*'
t_INTEGER = r'\d+'
t_FLOAT = r'((\d*\.\d+)(E[\+-]?\d+)?|([1-9]\d*E[\+-]?\d+))'
t_QUOT = r'"'
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
    
# --- Parser

# Write functions for each grammar rule which is
# specified in the docstring.
def p_expression(p):
    '''
    expression : db DOT table DOT insert LPAREN LCURL term RCURL RPAREN
    '''

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

    # NEED FIX
    
def p_db_char(p):
    '''
    db : CHARACTER
    '''

    # NEED FIX
    
def p_table_char(p):
    '''
    table : CHARACTER
    '''

    # NEED FIX
    
def p_insert_char(p):
    '''
    insert : CHARACTER
    '''

    # NEED FIX
    
def p_value_string(p):
    '''
    value : QUOT CHARACTER QUOT
    '''

    # NEED FIX

def p_value_int(p):
    '''
    value : INTEGER
    '''

    # NEED FIX

def p_value_char(p):
    '''
    value : FLOAT
    '''

    # NEED FIX

def p_error(p):
    print(f'Syntax error at {p.value!r}')
    
# Build the parser
parser = yacc()

# Parse an expression
ast = parser.parse('db.products.insert({item:"card",qrt:15})')
print(ast)
