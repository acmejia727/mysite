# -*- coding: utf-8 -*-
import sys

from chirry_parser import *
from chirry_lexer import *


def usage():
    sys.stderr.write('Usage: chirry filename\n')
    sys.exit(1)

def main_chirry(x):
    global text
    text = x
    tokens = imp_lex(text)
    parse_result = imp_parse(tokens)
    if x == '':
        log = 'Digite porfavor el codigo'
        return log
    if not parse_result:
        log = '###-- > Uhy Parse error! papa, asta aqui por asta ya no voy, papi se esperaba ',tokens[len(tokens)-1],error_lexer()
        return log
    if parse_result:
        log = 'Valido'
        return log
    ast = parse_result.value
    env = {}
    ast.eval(env)
    for name in env:
        viariable= '%s: %s\n' % (name, env[name])
    print'\n###-- >Codigo causa\n'
    print (text)





