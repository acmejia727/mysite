# -*- coding: utf-8 -*-
import sys

from chirry_parser import *
from chirry_lexer import *
error_par=0
def error_parser():
    global error_par
    if error_par == 1:
        return 1
    else:
        return 0

def main_chirry(x):
    global error_par
    global text
    text = x
    tokens = imp_lex(text)
    parse_result = imp_parse(tokens)
    if x == '':
        log = 'Digite porfavor el codigo'
        return log
    if not parse_result:
        log = '###-- > Uhy Parse error! papa, asta aqui por asta ya no voy, papi no se esperaba ',tokens[len(tokens)-1],error_lexer()
        error_par=1
        return log
    if parse_result:
        log = 'Aro papa!! sintaxy correcta'
        error_par=0
        return log
    ast = parse_result.value
    env = {}
    ast.eval(env)
    for name in env:
        viariable= '%s: %s\n' % (name, env[name])







