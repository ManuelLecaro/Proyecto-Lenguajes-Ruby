import ply.yacc as yacc
import lexerRuby
tokens=lexerRuby.tokens
print(tokens)

#Definición de variables, asignación

def p_assign(p):
    '''assign : variable ASS expr
              | variable ASS sexpr'''

def p_math(p):
    '''math : term arith term
            | term arith math
            | variable asig term'''

def p_variable(p):
    '''variable : LOCAL
                | GLOBAL 
                | CONSTANTS 
                | INSTANCEVAR 
                | CLASSVAR'''

def p_asig(p):
    '''asig : ASS
            | ADDASS
            | SUBASS
            | MULASS
            | DIVASS
            | MODASS
            | EXPASS'''

def p_expr(p):
    '''expr :  expr arith term
             | term
             | variable'''

def p_sexpr(p):
    '''sexpr : sterm MUL term
             | sterm ADD sexpr
             | sterm'''

def p_term(p):
    '''term : NUMBER'''

def p_sterm(p):
    '''sterm : STRING'''

def p_arith(p):
    '''arith : EXP
             | MUL
             | DIV
             | MOD
             | ADD
             | SUB'''

def p_logic(p):
    '''logic : variable comparison variable
             | variable EQUAL FALSE
             | variable EQUAL TRUE
             | variable comparison term
             | variable comparison sterm
             | logic logcompare logic'''

def p_comparison(p):
    '''comparison : EQUAL
                  | NOTEQ
                  | GREATHER
                  | LOWER
                  | GREATHEREQ
                  | LOWEREQ'''

def p_logcompare(p):
    '''logcompare : ANDLOG
                  | ORLOG
                  | NOTLOG
                  | AND
                  | OR
                  | NOT'''
    
def p_error(p):
    '''error: error'''

yacc.yacc()