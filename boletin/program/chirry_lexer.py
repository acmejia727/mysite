import sys
import re
error_sw=0
error_lex=''
RESERVED = 'RESERVED'
INT      = 'INT'
ID       = 'ID'

token_exprs = [
    (r'[ \n\t]+',              None),
    (r'#[^\n]*',               None),
    (r'\s+',                    None),
    (r'\->',                   RESERVED),#asignacion
    (r'\(',                    RESERVED),
    (r'\)',                    RESERVED),
    (r':',                     RESERVED),
    (r'\+',                    RESERVED),
    (r'-',                     RESERVED),
    (r'\*',                    RESERVED),
    (r'/',                     RESERVED),
    (r'<=',                    RESERVED),
    (r'<',                     RESERVED),
    (r'>=',                    RESERVED),
    (r'>',                     RESERVED),
    (r'!=',                    RESERVED),
    (r'=',                     RESERVED),
    (r'Y',                   RESERVED),#and
    (r'O',                    RESERVED),#or
    (r'NO',                   RESERVED),#not
    (r'ESOVA',                    RESERVED),#if
    (r'COMOJUE',                  RESERVED),#then
    (r'PORKAJA',                  RESERVED),#else
    (r'AIJUE',                 RESERVED),#while
    (r'SINOVA',                    RESERVED),#do
    (r'ASTAQUI',                   RESERVED),#end
    (r'[0-9]+',                INT),
    (r'[A-Za-z][A-Za-z0-9_]*', ID),
]

def lex(characters, token_exprs):
    global error_sw
    global error_lex

    pos = 0
    tokens = []
    cont=0
    cont_line=0


    while pos < len(characters):
        match = None
        for token_expr in token_exprs:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(characters, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag)
                    tokens.append(token)
                    cont = cont + 1
                break
        if not match:
            error_lex= 'Caracter Ilegal, suave nano que tu no sabes escribir: =  %s' % characters[pos]
            error_sw=1
            print cont_line
            return tokens
            sys.exit(1)
        else:
            pos = match.end(0)
    error_sw = 0
    return tokens

def imp_lex(characters):
    return lex(characters, token_exprs)

def error_lexer():
    global error_sw
    global error_lex
    if error_sw == 1:
        msj=error_lex
    else:
        msj=''
    return msj