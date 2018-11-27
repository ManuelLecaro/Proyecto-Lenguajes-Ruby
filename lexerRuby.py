import ply.lex as lex

reservadas={'alias':'ALIAS','and':'AND','begin':'BEGIN','break':'BREAK','case':'CASE','class':'CLASS','def':'DEF','defined?':'DEFINED'
                    ,'do':'DO','else':'ELSE','elsif':'ELSIF','end':'END','ensure':'ENSURE','false':'FALSE','for':'FOR','if':'IF'
                    ,'in':'IN','module':'MODULE','next':'NEXT','nil':'NIL','not':'NOT','or':'OR','redo':'REDO','rescue':'RESCUE'
                    ,'retry':'RETRY','return':'RETURN','self':'SELF','super':'SUPER','then':'THEN','true':'TRUE','undef':'UNDEF'
                    ,'unless':'UNLESS','until':'UNTIL','when':'WHEN','while':'WHILE','yield':'YIELD','_FILE_':'FILE','_LINE_':'LINE'}

tokens = ['LOCAL', 'GLOBAL', 'CONSTANTS', 'INSTANCEVAR','CLASSVAR','PSEUDO','ERROR',
        #BASIC DATA TYPES
        'NUMBER', 'STRING','BOOLEAN','INT','FLOAT',
        #ARITHMETIC OPERATORS
        'EXP','MUL','DIV','MOD','ADD','SUB',
        #BASIC COMPARISON OPERATORS
        'EQUAL','NOTEQ','GREATHER','LOWER','GREATHEREQ','LOWEREQ',
        #ASSIGMENT OPERATORS
        'ASS','ADDASS','SUBASS','MULASS','DIVASS','MODASS','EXPASS',
        #BASIC LOGICAL OPERATORS
        'ANDLOG','ORLOG','NOTLOG',
        #OTHERS
        'LBRACK','RBRACK','COMA','DOBLEPOINT','DOUBLESECUENCEPOINT',
        ]+list(reservadas.values())

t_LOCAL = r'^(_|[a-z])[a-zA-Z0-9_]*'
t_GLOBAL = r'\$[a-zA-Z][a-zA-Z0-9_]*'
t_CONSTANTS = r'^[A-Z][A-Z0-9_]*'
t_INSTANCEVAR = r'^@[a-zA-Z][a-zA-Z0-9_]*'
t_CLASSVAR = r'^@@[a-zA-Z][a-zA-Z0-9_]*'
t_PSEUDO = r'self|true|false|nil|__FILE__|__LINE__'

#BASIC DATA TYPES
t_NUMBER = r'[0-9]+((\.[0-9]+))?'
t_STRING = r'[a-z\_]+'
t_BOOLEAN = r'true|false'
t_INT = r'^[0-9]+'
t_FLOAT = r'^[0,9]*.[0-9]+'

#ARITHMETIC OPERATORS
t_EXP = r'^\*\*'
t_MUL = r'^\*'
t_DIV = r'^/'
t_MOD =  r'^%'
t_ADD =  r'^\+'
t_SUB = r'^-'
#BASIC COMPARISON OPERATORS
t_EQUAL = r'^=='
t_NOTEQ = r'^!='
t_GREATHER = r'^>'
t_LOWER = r'^<'
t_GREATHEREQ = r'^>='
t_LOWEREQ = r'^<='
#ASSIGMENT OPERATORS
t_ASS = r'^='
t_ADDASS = r'^\+='
t_SUBASS = r'^-='
t_MULASS = r'^\*='
t_DIVASS = r'^/='
t_MODASS = r'^%='
t_EXPASS = r'^\*\*='
#BASIC LOGICAL OPERATORS
t_ANDLOG = r'^&&'
t_ORLOG = r'^\|\|'
t_NOTLOG = r'^!'
#OTHERS
t_LBRACK = r'\['
t_RBRACK = r'\]'
t_COMA = r','
t_DOBLEPOINT = r':'
t_DOUBLESECUENCEPOINT = r'..'




def t_error(token):
    salida = "\ntype:" + token.type
    salida += "\nvalue:" + str(token.value)
    salida += "\nline:" + str(token.lineno)
    salida += "\nposition:" + str(token.lexpos)
    print (salida)
    token.lexer.skip(1)
def t_ALIAS(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'ALIAS')
    return t
def t_AND(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'AND')
    return t
def t_BREAK(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'BREAK')
    return t
def t_BEGIN(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'BEGIN')
    return t
def t_CASE(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'CASE')
    return t
def t_CLASS(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'CLASS')
    return t
def t_DEF(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'DEF')
    return t
def t_DEFINED(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'DEFINED')
    return t
def t_DO(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'DO')
    return t
def t_ELSE(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'ELSE')
    return t
def t_ELSIF(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'ELSIF')
    return t
def t_END(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'END')
    return t
def t_ENSURE(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'ENSURE')
    return t
def t_FALSE(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'FALSE')
    return t
def t_FOR(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'FOR')
    return t
def t_IF(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'IF')
    return t
def t_IN(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'IN')
    return t
def t_MODULE(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'MODULE')
    return t
def t_NEXT(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'NEXT')
    return t
def t_NIL(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'NIL')
    return t
def t_NOT(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'NOT')
    return t
def t_OR(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'OR')
    return t
def t_REDO(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'REDO')
    return t
def t_RESCUE(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'RESCUE')
    return t
def t_RETRY(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'RETRY')
    return t
def t_RETURN(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'RETURN')
    return t
def t_SELF(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'SELF')
    return t
def t_SUPER(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'SUPER')
    return t
def t_THEN(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'THEN')
    return t
def t_TRUE(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'TRUE')
    return t
def t_UNDEF(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'UNDEF')
    return t
def t_UNLESS(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'UNLESS')
    return t
def t_UNTIL(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'UNTIL')
    return t
def t_WHEN(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'WHEN')
    return t
def t_WHILE(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'WHILE')
    return t
def t_YIELD(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'YIELD')
    return t
def t_FILE(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'FILE')
    return t
def t_LINE(t):
    r'[a-z\_]+'
    t.type=reservadas.get(t.value,'LINE')
    return t

lex.lex()

#texter = ['CONSTANTE', '4local','_local', '$global','@instance', '@@clase_', '@peso',"self",'4',
#                'alias','def','for','if','and','super','lista',
#                '**','*','/','%','+','-',
#               '==','!=','>','<','>=','<=',
#               '=','+=','-=','*=','/=','%=','**=',
#                '&&','||','!'
#               ]

#for i in texter:
#    lex.input(i)
#    token = lex.token()
#   while token is not None:
#        print(token.type)
#        token = lex.token()

