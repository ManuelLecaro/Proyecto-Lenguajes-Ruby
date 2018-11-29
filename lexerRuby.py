import ply.lex as lex

reservadas={'alias':'ALIAS','and':'AND','begin':'BEGIN','break':'BREAK','case':'CASE','class':'CLASS','def':'DEF','defined?':'DEFINED'
                    ,'do':'DO','else':'ELSE','elsif':'ELSIF','end':'END','ensure':'ENSURE','false':'FALSE','for':'FOR','if':'IF'
                    ,'in':'IN','module':'MODULE','next':'NEXT','nil':'NIL','not':'NOT','or':'OR','redo':'REDO','rescue':'RESCUE'
                    ,'retry':'RETRY','return':'RETURN','self':'SELF','super':'SUPER','then':'THEN','true':'TRUE','undef':'UNDEF'
                    ,'unless':'UNLESS','until':'UNTIL','when':'WHEN','while':'WHILE','yield':'YIELD','_FILE_':'FILE','_LINE_':'LINE'}

tokens = ['LOCAL', 'GLOBAL', 'CONSTANTS', 'INSTANCEVAR','CLASSVAR','PSEUDO','ERROR',
        #BASIC DATA TYPES
        'NUMBER', 'STRING','INT','FLOAT', #'BOOLEAN'
        #ARITHMETIC OPERATORS
        'EXP','MUL','DIV','MOD','ADD','SUB',
        #BASIC COMPARISON OPERATORS
        'EQUAL','NOTEQ','GREATHER','LOWER','GREATHEREQ','LOWEREQ',
        #ASSIGMENT OPERATORS
        'ASS','ADDASS','SUBASS','MULASS','DIVASS','MODASS','EXPASS',
        #BASIC LOGICAL OPERATORS
        'ANDLOG','ORLOG','NOTLOG',
        #OTHERS
        'LBRACK','RBRACK','COMA','DOBLEPOINT','DOUBLESECUENCEPOINT', "NEWLINE"
        ]+list(reservadas.values())

def t_LOCAL(t):
    r'^(_|[a-z])([a-zA-Z0-9_])*'
    t.type=reservadas.get(t.value,'LOCAL')
    return t

def t_GLOBAL(t):
    r'^\$[a-zA-Z]([a-zA-Z0-9_])*'
    t.type=reservadas.get(t.value,'GLOBAL')
    return t

def t_CONSTANTS(t):
    r'^[A-Z]([A-Z0-9_])*'
    t.type=reservadas.get(t.value,'CONSTANTS')
    return t

def t_INSTANCEVAR(t):
    r'@[a-zA-Z]([a-zA-Z0-9_])*'
    t.type=reservadas.get(t.value,'INSTANCEVAR')
    return t

def t_CLASSVAR(t):
    r'@@[a-zA-Z]([a-zA-Z0-9_])*'
    t.type=reservadas.get(t.value,'CLASSVAR')
    return t

def t_PSEUDO(t):
    r'self|true|false|nil|__FILE__|__LINE__'
    t.type=reservadas.get(t.value,'PSEUDO')
    return t

def t_NEWLINE(t):
    r'\n+'    

t_ignore = ' \t\r'

#BASIC DATA TYPES
t_STRING = r'"[a-z\_]+"'
# t_BOOLEAN = r'true|false'


#ARITHMETIC OPERATORS
t_EXP = r'\*\*'
t_MUL = r'\*'
t_DIV = r'/'
t_MOD =  r'%'
t_ADD =  r'\+'
t_SUB = r'-'
#BASIC COMPARISON OPERATORS
t_EQUAL = r'=='
t_NOTEQ = r'!='
t_GREATHER = r'>'
t_LOWER = r'<'
t_GREATHEREQ = r'>='
t_LOWEREQ = r'<='
#ASSIGMENT OPERATORS
t_ASS = r'='
t_ADDASS = r'\+='
t_SUBASS = r'-='
t_MULASS = r'\*='
t_DIVASS = r'/='
t_MODASS = r'%='
t_EXPASS = r'\*\*='
#BASIC LOGICAL OPERATORS
t_ANDLOG = r'&&'
t_ORLOG = r'\|\|'
t_NOTLOG = r'!'
#OTHERS
t_LBRACK = r'\['
t_RBRACK = r'\]'
t_COMA = r'\,'
t_DOBLEPOINT = r'\:'
t_DOUBLESECUENCEPOINT = r'\.\.'


def t_NUMBER(t):
     r'(-)?[0-9]+((\.[0-9]+))?'
     t.value = float(t.value)    
     return t

def t_error(token):
    salida = "\ntype:" + token.type
    salida += "\nvalue:" + str(token.value)
    salida += "\nline:" + str(token.lineno)
    salida += "\nposition:" + str(token.lexpos)
    print (salida)
    token.lexer.skip(1)
def t_ALIAS(t):
    r'ALIAS'
    t.type=reservadas.get(t.value,'ALIAS')
    return t
def t_AND(t):
    r'AND'
    t.type=reservadas.get(t.value,'AND')
    return t
def t_BREAK(t):
    r'BREAK'
    t.type=reservadas.get(t.value,'BREAK')
    return t
def t_BEGIN(t):
    r'BEGIN'
    t.type=reservadas.get(t.value,'BEGIN')
    return t
def t_CASE(t):
    r'CASE'
    t.type=reservadas.get(t.value,'CASE')
    return t
def t_CLASS(t):
    r'CLASS'
    t.type=reservadas.get(t.value,'CLASS')
    return t
def t_DEF(t):
    r'DEF'
    t.type=reservadas.get(t.value,'DEF')
    return t
def t_DEFINED(t):
    r'DEFINED'
    t.type=reservadas.get(t.value,'DEFINED')
    return t
def t_DO(t):
    r'DO'
    t.type=reservadas.get(t.value,'DO')
    return t
def t_ELSE(t):
    r'ELSE'
    t.type=reservadas.get(t.value,'ELSE')
    return t
def t_ELSIF(t):
    r'ELSIF'
    t.type=reservadas.get(t.value,'ELSIF')
    return t
def t_END(t):
    r'END'
    t.type=reservadas.get(t.value,'END')
    return t
def t_ENSURE(t):
    r'ENSURE'
    t.type=reservadas.get(t.value,'ENSURE')
    return t
def t_FALSE(t):
    r'FALSE'
    t.type=reservadas.get(t.value,'FALSE')
    return t
def t_FOR(t):
    r'FOR'
    t.type=reservadas.get(t.value,'FOR')
    return t
def t_IF(t):
    r'IF'
    t.type=reservadas.get(t.value,'IF')
    return t
def t_IN(t):
    r'IN'
    t.type=reservadas.get(t.value,'IN')
    return t
def t_MODULE(t):
    r'MODULE'
    t.type=reservadas.get(t.value,'MODULE')
    return t
def t_NEXT(t):
    r'NEXT'
    t.type=reservadas.get(t.value,'NEXT')
    return t
def t_NIL(t):
    r'NIL'
    t.type=reservadas.get(t.value,'NIL')
    return t
def t_NOT(t):
    r'NOT'
    t.type=reservadas.get(t.value,'NOT')
    return t
def t_OR(t):
    r'OR'
    t.type=reservadas.get(t.value,'OR')
    return t
def t_REDO(t):
    r'REPO'
    t.type=reservadas.get(t.value,'REDO')
    return t
def t_RESCUE(t):
    r'RESCUE'
    t.type=reservadas.get(t.value,'RESCUE')
    return t
def t_RETRY(t):
    r'RETRY'
    t.type=reservadas.get(t.value,'RETRY')
    return t
def t_RETURN(t):
    r'RETURN'
    t.type=reservadas.get(t.value,'RETURN')
    return t
def t_SELF(t):
    r'SELF'
    t.type=reservadas.get(t.value,'SELF')
    return t
def t_SUPER(t):
    r'SUPER'
    t.type=reservadas.get(t.value,'SUPER')
    return t
def t_THEN(t):
    r'THEN'
    t.type=reservadas.get(t.value,'THEN')
    return t
def t_TRUE(t):
    r'TRUE'
    t.type=reservadas.get(t.value,'TRUE')
    return t
def t_UNDEF(t):
    r'UNDEF'
    t.type=reservadas.get(t.value,'UNDEF')
    return t
def t_UNLESS(t):
    r'UNLESS'
    t.type=reservadas.get(t.value,'UNLESS')
    return t
def t_UNTIL(t):
    r'UNTIL'
    t.type=reservadas.get(t.value,'UNTIL')
    return t
def t_WHEN(t):
    r'WHEN'
    t.type=reservadas.get(t.value,'WHEN')
    return t
def t_WHILE(t):
    r'WHILE'
    t.type=reservadas.get(t.value,'WHILE')
    return t
def t_YIELD(t):
    r'YIELD'
    t.type=reservadas.get(t.value,'YIELD')
    return t
def t_FILE(t):
    r'FILE'
    t.type=reservadas.get(t.value,'FILE')
    return t
def t_LINE(t):
    r'LINE'
    t.type=reservadas.get(t.value,'LINE')
    return t

lex.lex()

texter = ['CONSTANTE', '4local','_local', '$global','@instance', '@@clase_', '@peso',"self",'4',
                'alias','def','for','if','and','super','lista',
                '**','*','/','%','+','-',
               '==','!=','>','<','>=','<=',
               '=','+=','-=','*=','/=','%=','**=',
                '&&','||','!','"string"'
               ]

# for i in texter:
#    lex.input(i)
#    token=lex.token()
#    while token is not None:
#        print(token.type)
#        token = lex.token()

