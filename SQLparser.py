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
# GOAL
#     Input : db.products.insert({item:"card",qrt:15})
#     Output : INSERT INTO products (item, qrt) VALUES ('card', 15)
# ------------------------------------------------------------------------------
# TO DO
#
# 1. insert method인지 확인
#   - input이 'abcd'일 때 => Not insert method
#   - input이 'db.products.drop({writeConcern: document})'일 때 => Not insert method
# 2. 원래 있던 column인가?
#   - db에 존재하는 column list 만들기
#   - item과 qrt가 list에 존재하는 지 확인하는 부분 추가
# 3. Output
#   - 원래 없던 column일 경우 : ALTER TABLE products ADD COLUMN item VARCHAR(255), ADD COLUMN qrt int;\nINSERT INTO products (item, qrt) VALUES ('card', 15);
#   - 원래 있는 column일 경우 : INSERT INTO products (item, qrt) VALUES ('card', 15);
# ------------------------------------------------------------------------------

from src.ply.lex import lex
from src.ply.yacc import yacc

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
t_COLON = r'\:'
t_LCURL = r'\{'
t_RCURL = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r'\,'
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

db_name = []
table_name = []
item = {}

# Write functions for each grammar rule which is
# specified in the docstring.
def p_expression(p):
    '''
    expression : db DOT table DOT insert LPAREN LCURL term RCURL RPAREN
    '''

    db_name.append(p[1])
    table_name.append(p[3])

    # Check method
    if p[5] == 'insert':
        pass
    else:
        raise Exception("not insert method")
    print("")

def p_term(p):
    '''
    term : key COLON value
         | term COMMA term
    '''

    if p[2] == ',':
        pass
    else:
        item[p[1]] = p[3]
    

def p_key_char(p):
    '''
    key : CHARACTER
    '''

    p[0] = p[1]
    # print(p[0])
    
def p_db_char(p):
    '''
    db : CHARACTER
    '''

    p[0] = p[1]
    # print(p[0])

def p_table_char(p):
    '''
    table : CHARACTER
    '''

    p[0] = p[1]
    # print(p[0])
    
def p_insert_char(p):
    '''
    insert : CHARACTER
    '''

    p[0] = p[1]
    # print(p[0])
    
def p_value_string(p):
    '''
    value : QUOTE CHARACTER QUOTE
    '''

    p[0] = f"{p[1]}{p[2]}{p[3]}"
    # print(p[0])

def p_value_int(p):
    '''
    value : INTEGER
    '''

    p[0] = p[1]
    # print(p[0])

def p_value_char(p):
    '''
    value : FLOAT
    '''

    p[0] = p[1]
    # print(p[0])

def p_error(p):
    print(f'Syntax error at {p.value!r}')
    
# Build the parser
parser = yacc()

# Parse an expression
ast = parser.parse('db.products.insert({item:"card",qrt:15})')
# ast = parser.parse('abcd')
# ast = parser.parse('db.products.drop({writeConcern: document})')

print('Database name: ', db_name)
print('Table name: ', table_name)
print('Item to insert: ', item)
print('SQL code :')
# print(output)
