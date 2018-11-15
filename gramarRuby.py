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
             | variable
             | assign'''

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
             | variable EQUAL BOOLEAN
             | variable comparison term
             | variable comparison sterm
             | logic logcompare logic
             | logic logcompare BOOLEAN
             | BOOLEAN logcompare BOOLEAN
             | BOOLEAN logcompare logic
             | term comparison variable
             | sterm comparison variable
             '''

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
#Definicion de la estructuras de condicion y lazos
def p_salto(p):
    '''salto : \n '''
# def p_puntos(p):
#     '''puntos : ":"'''
def p_if(p):
    '''if : IF logic salto expr salto
          | IF logic THEN salto expr salto
          | if END
          | if else END
          | if elsif END'''
def p_else(p):
    '''else : ELSE salto expr salto '''
def p_elsif(p):
    '''elsif : ELSIF logic salto expr salto
             | ELSIF logic THEN salto expr salto
             | elsif elsif
             | elsif else'''
def p_code(p):
    '''code : expr
            | if'''
# def p_while(p):
#     '''while : WHILE logic salto code salto END
#              | WHILE logic DO salto code END
#              | WHILE  logic DOBLEPOIN code END
#              | while while
#              | BEGIN salto code END WHILE logic'''
def p_while(p):
    '''while : WHILE logic salto code salto END
             | WHILE logic DO salto code END
             | WHILE  logic DOBLEPOINT code END
             | BEGIN salto code END WHILE logic'''
def p_iterador(p):
    '''iterador : variable
                | variable "," variable'''
def p_expresiones(p):
    '''expresiones : term DOUBLESECUENCEPOINT term'''
def p_for(p):
    '''for : FOR iterador IN expresiones salto code salto END
           | FOR iterador IN expresiones DO salto code salto END
           | FOR iterador IN array salto code salto END
           | FOR iterador IN array DO salto code salto END'''

def p_array(p):
    '''array : LBRACK defarray RBRACK'''

def p_defarray(p):
    '''defarray : NUMBER 
                | NUMBER COMA defarray
                | STRING
                | STRING COMA defarray
                | INT
                | INT COMA defarray
                | FLOAT
                | FLOAT COMA defarray
                | BOOLEAN
                | BOOLEAN COMA defarray'''

def p_assarray(p):
    '''assarray : variable ASS array
                | array'''

def p_index(p):
    '''index : variable LBRACK INT RBRACK'''

def p_slice(p):
    '''slice : variable LBRACK defslice RBRACK'''

def p_defslice(p):
    '''defslice : INT DOBLEPOINT INT
                    | INT DOBLEPOINT
                    | DOBLEPOINT INT'''

yacc.yacc()