import ply.yacc as yacc
import lexerRuby
import ASTsRuby
tokens=lexerRuby.tokens
print(tokens)

#Definición de variables, asignación

def p_assign(p):
    '''assign : variable ASS expr
              | variable ASS sexpr'''
    p[0] = ASTsRuby.Assign(p[1], p[2], p[3])

def p_math(p):
    '''math : term arith term
            | term arith math
            | variable asig term'''
    p[0] = ASTsRuby.Math(p[1],p[2],p[3])

def p_variable(p):
    '''variable : LOCAL
                | GLOBAL 
                | CONSTANTS 
                | INSTANCEVAR 
                | CLASSVAR'''
    p[0] = p[1]

def p_asig(p):
    '''asig : ASS
            | ADDASS
            | SUBASS
            | MULASS
            | DIVASS
            | MODASS
            | EXPASS'''
    p[0] = p[1]

def p_expr(p):
    '''expr :  math
             | term
             | variable
             | assign'''
    p[0] = p[1]
    

def p_sexpr(p):
    '''sexpr : sterm MUL term
             | sterm ADD sexpr
             | sterm'''


def p_term(p):
    '''term : NUMBER'''
    p[0] = p[1]

def p_sterm(p):
    '''sterm : STRING'''
    p[0] = p[1]

def p_arith(p):
    '''arith : EXP
             | MUL
             | DIV
             | MOD
             | ADD
             | SUB'''
    p[0] = p[1]

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
    p[0] = ASTsRuby.Logical(p[1], p[2], p[3])

def p_comparison(p):
    '''comparison : EQUAL
                  | NOTEQ
                  | GREATHER
                  | LOWER
                  | GREATHEREQ
                  | LOWEREQ'''
    p[0] = p[1]

def p_logcompare(p):
    '''logcompare : ANDLOG
                  | ORLOG
                  | NOTLOG
                  | AND
                  | OR
                  | NOT'''
    p[0] = p[1] 

def p_error(p):
    '''error: error'''

#Definicion de la estructuras de condicion y lazos
def p_salto(p):
    '''salto : NEWLINE '''
    p[0] = p[1]

# def p_puntos(p):
#     '''puntos : ":"'''

def p_if(p):
    '''if : IF logic salto expr salto
          | IF logic THEN salto expr salto
          | if END
          | if else END
          | if elsif END'''
    p[0] = ASTsRuby.IfAST(p[1], p[2], p[3], p[4],p[5])

def p_else(p):
    '''else : ELSE salto expr salto '''
    p[0] = ASTsRuby.ElseAST(p[1],p[2],p[3],p[4])

def p_elsif(p):
    '''elsif : ELSIF logic salto expr salto
             | ELSIF logic THEN salto expr salto
             | elsif elsif
             | elsif else'''
    p[0] = ASTsRuby.ElseifAST(p[1], p[2], p[3], p[4],p[5])

def p_code(p):
    '''code : expr
            | if'''
    p[0] = p[1]

# def p_while(p):
#     '''while : WHILE logic salto code salto END
#              | WHILE logic DO salto code END
#              | WHILE  logic DOBLEPOIN code END
#              | while while
#              | BEGIN salto code END WHILE logic'''
def p_while(p):
    '''while : WHILE logic code END
             | WHILE logic DO salto code END
             | WHILE  logic DOBLEPOINT code END
             | BEGIN salto code END WHILE logic'''
    p[0] = ASTsRuby.WhileAST(p[1], p[2], p[3], p[4],p[5], p[6])

def p_iterador(p):
    '''iterador : variable
                | variable "," variable'''
    p[0] = ASTsRuby.IteratorAST(p[1], p[2], p[3])
    
def p_expresiones(p):
    '''expresiones : term DOUBLESECUENCEPOINT term'''
    p[0] = ASTsRuby.ExpAST(p[1], p[2], p[3])

def p_for(p):
    '''for : FOR iterador IN expresiones salto code salto END
           | FOR iterador IN expresiones DO salto code salto END
           | FOR iterador IN array salto code salto END
           | FOR iterador IN array DO salto code salto END'''
    p[0] = ASTsRuby.ForAST(p[1], p[2], p[3], p[4],p[5], p[6], p[7], p[8])    

def p_array(p):
    '''array : LBRACK defarray RBRACK'''
    p[0] = p[2]

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
    p[0] = ASTsRuby.ArrayAST(p[1], p[2], p[3])

    

def p_assarray(p):
    '''assarray : variable ASS array
                | array'''
    p[0] = ASTsRuby.AsArrayAST(p[1], p[2], p[3])

def p_index(p):
    '''index : variable LBRACK INT RBRACK'''
    p[0] = ASTsRuby.IndexAST(p[1], p[2], p[3], p[4])

def p_slice(p):
    '''slice : variable LBRACK defslice RBRACK'''
    p[0] = ASTsRuby.SlideAST(p[1], p[2], p[3], p[4])

def p_defslice(p):
    '''defslice : INT DOBLEPOINT INT
                    | INT DOBLEPOINT
                    | DOBLEPOINT INT'''
    p[0] = ASTsRuby.DefSlideAST(p[1], p[2], p[3])
    

parser = yacc.yacc()

print(parser.parse("while i < 10 do \n a = 1 end"))

