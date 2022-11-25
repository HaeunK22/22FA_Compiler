# -----------------------------------------------------------------------------
# example.py
#
# Example of using PLY To parse the following simple grammar.
#
#   expression : term PLUS term
#              | term MINUS term
#              | term
#
#   term       : factor TIMES factor
#              | factor DIVIDE factor
#              | factor
#
#   factor     : NUMBER
#              | NAME
#              | PLUS factor
#              | MINUS factor
#              | LPAREN expression RPAREN
#
# -----------------------------------------------------------------------------
# SQLparser.py
#
#   expression : DB DOT TABLE DOT INSERT LPAREN LCURL term RCURL RPAREN
#
#   term : KEY COLON value
#        | term COMMA term
#
#   value : CHARACTER
#         | INTEGER
#         | FLOAT

from ply.lex import lex
from ply.yacc import yacc

# --- Tokenizer

# All tokens must be named in advance.
# tokens = ( 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN',
#           'NAME', 'NUMBER' )
tokens = ('CHARACTER', 'INTEGER', 'FLOAT', 'KEY', 'COLON', 'LCURL', 'RCURL', 'LPAREN', 'RPAREN', 'COMMA', 'INSERT', 'DB', 'TABLE', 'DOT')

# Ignored characters
t_ignore = ' \t'

# Token matching rules are written as regexs
# t_PLUS = r'\+'
# t_MINUS = r'-'
# t_TIMES = r'\*'
# t_DIVIDE = r'/'
# t_LPAREN = r'\('
# t_RPAREN = r'\)'
# t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_CHARACTER = r'[a-zA-Z_][a-zA-Z_]*'
t_INTEGER = r'[]'
t_FLOAT = r''
t_KEY = r'[a-zA-Z_][a-zA-Z_]*'
t_COLON = r'\:'
t_LCURL = r'\{'
t_RCURL = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r'\,'
t_INSERT = r'\insert'
t_DB = r'[a-zA-Z_][a-zA-Z_]*'
t_TABLE = r'[a-zA-Z_][a-zA-Z_]*'
t_DOT = r'\.'

# A function can be used if there is an associated action.
# Write the matching regex in the docstring.
# def t_NUMBER(t):
#     r'\d+'
#     t.value = int(t.value)
#     return t

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
# def p_expression(p):
#     '''
#     expression : term PLUS term
#                | term MINUS term
#     '''
#     # p is a sequence that represents rule contents.
#     #
#     # expression : term PLUS term
#     #   p[0]     : p[1] p[2] p[3]
#     # 
#     p[0] = ('binop', p[2], p[1], p[3])

# def p_expression_term(p):
#     '''
#     expression : term
#     '''
#     p[0] = p[1]

def p_expression(p):
    '''
    expression : DB DOT TABLE DOT INSERT LPAREN LCURL term RCURL RPAREN
    '''

    # NEED FIX

# def p_term(p):
#     '''
#     term : factor TIMES factor
#         | factor DIVIDE factor
#     '''
#     p[0] = ('binop', p[2], p[1], p[3])

# def p_term_factor(p):
#     '''
#     term : factor
#     '''
#     p[0] = p[1]

def p_term(p):
    '''
    term : KEY COLON value
        | term COMMA term
    '''

    # NEED FIX

# def p_factor_number(p):
#     '''
#     factor : NUMBER
#     '''
#     p[0] = ('number', p[1])

# def p_factor_name(p):
#     '''
#     factor : NAME
#     '''
#     p[0] = ('name', p[1])

# def p_factor_unary(p):
#     '''
#     factor : PLUS factor
#            | MINUS factor
#     '''
#     p[0] = ('unary', p[1], p[2])

# def p_factor_grouped(p):
#     '''
#     factor : LPAREN expression RPAREN
#     '''
#     p[0] = ('grouped', p[2])

def p_value_char(p):
    '''
    value : CHARACTER
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
ast = parser.parse('2 * 3 + 4 * (5 - x)')
print(ast)
