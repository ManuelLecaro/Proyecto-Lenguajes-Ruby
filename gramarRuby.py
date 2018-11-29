import ply.yacc as yacc
import lexerRuby
import ASTsRuby

tokens=lexerRuby.tokens

def p_code(p):
    '''code : expr
            | if
            | while
            | expresiones
            | for
            | assign
            | code code'''
    p[0] = p[1]
    if(len(p)==3):
        ASTsRuby.CodeAST(p[1], p[2])

def p_while(p):
    '''while : WHILE logical code END
             | WHILE logical DO salto code salto END
             | WHILE logical DOBLEPOINT salto code salto END
             | BEGIN code END WHILE logical'''
    if(len(p)==7):
            p[0] = ASTsRuby.WhileAST(p[1], p[2], p[3], p[4],p[5], p[6])
    if(len(p)==6):
            p[0] = ASTsRuby.WhileAST_s(p[1], p[2], p[3], p[4],p[5])
    if(len(p)==5):
            p[0] = ASTsRuby.WhileAST_c(p[1], p[2], p[3], p[4],p[5])

def p_logical(p):
    '''logical : term comparison term
               | term comparison logical
               | variable comparison term
               | variable comparison BOOLEAN
               | logical logcompare logical
               | BOOLEAN'''
    if(len(p)==3):
        ASTsRuby.Logical(p[1], p[2], p[3])
    else:
        p[0] = p[1]


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

def p_assign(p):
    '''assign : variable ASS expr
              | variable ASS sexpr
              | variable ASS array'''
    p[0] = ASTsRuby.Assign(p[1], p[2], p[3])
    print(p[0])

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
             | sterm
             | variable
             | slice
             | index'''
    p[0] = p[1]
    

def p_sexpr(p):
    '''sexpr : sterm MUL term
             | sterm ADD sexpr'''
    if(len(p)==4):
        ASTsRuby.SexprAST(p[1], p[2], p[3])
    if(len(p)==2):
        p[0] = p[1]

def p_term(p):
    '''term : NUMBER'''
    p[0] = ASTsRuby.NumberAST(p[1])

def p_sterm(p):
    '''sterm : STRING'''
    p[0] = ASTsRuby.StringAST(p[1])

def p_arith(p):
    '''arith : EXP
             | MUL
             | DIV
             | MOD
             | ADD
             | SUB'''
    p[0] = p[1]

def p_for(p):
    '''for : FOR iterador IN expresiones code END
           | FOR iterador IN expresiones DO code END
           | FOR iterador IN array code END
           | FOR iterador IN array DO code END'''
    p[0] = ASTsRuby.ForAST(p[1], p[2], p[3], p[4],p[5], p[6], p[7], p[8])    


def p_salto(p):
    '''salto : NEWLINE '''
    p[0] = p[1]

"""Definicion de la estructuras de condicion y lazos"""

def p_if(p):
    '''if : IF logical expr END
          | IF logical THEN expr END
          | IF logical
          | IF logical THEN
          | if else
          | if elsif END'''
    if(len(p)==6):
        p[0] = ASTsRuby.IfAST(p[1], p[2], p[3], p[4],p[5])
    if(len(p)==5):
        p[0] = ASTsRuby.IfAST_f(p[1], p[2], p[3], p[4])
    if(len(p)==4):
        p[0] = ASTsRuby.IfAST_t(p[1], p[2], p[3])
    if(len(p)==3):
        p[0] = ASTsRuby.IfAST_d(p[1], p[2])

def p_else(p):
    '''else : ELSE code END'''
    p[0] = ASTsRuby.ElseAST(p[1],p[2],p[3])

def p_elsif(p):
    '''elsif : ELSIF logical final'''
    if(len(p)==5):
        p[0] = ASTsRuby.ElseifAST(p[1], p[2], p[3], p[4])
    if(len(p)==4):
        p[0] = ASTsRuby.ElseifAST_t(p[1], p[2], p[3])

def p_final(p):
    '''final : code
             | THEN code
             | code else
             | code elsif '''
    if(len(p)==3):
        p[0] = ASTsRuby.FinalAST(p[1], p[2])
    else:
        p[0] = p[1]

def p_iterador(p):
    '''iterador : variable
                | variable COMA variable'''
    p[0] = ASTsRuby.IteratorAST(p[1], p[2], p[3])
    
def p_expresiones(p):
    '''expresiones : term DOUBLESECUENCEPOINT term'''
    p[0] = ASTsRuby.ExpAST(p[1], p[2], p[3])


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

def p_error(p):
    if(p):
        print("SYNTACTIC ERROR: line:", p.lexer.lineno, "position:", p.lexpos, "Syntax error:", p.value)
    else:
        print("SYNTACTIC ERROR: Unknown syntax error")

    
parser = yacc.yacc()

string =  ' variable = 4 '

print(parser.parse(string))

