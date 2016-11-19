# -*- coding: utf-8 -*-
import sys

from chirry_parser import *
from chirry_lexer import *
error_par=0
variable=[]
def error_parser():
    global error_par
    if error_par == 1:
        return 1
    else:
        return 0

def main_chirry(x):
    global variable
    global error_par
    global text
    variable=[]
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
        ast = parse_result.value
        env = {}
        ast.eval(env)
        for name in env:
            variable.append('%s = %s' % (name, env[name]))
            print variable
        return log

def variables():
    global variable
    return variable




