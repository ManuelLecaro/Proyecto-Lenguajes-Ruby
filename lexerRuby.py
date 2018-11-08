import ply.lex as lex

tokens = ['LOCAL', 'GLOBAL', 'CONSTANTS', 'INSTANCEVAR','CLASSVAR','PSEUDO','ERROR' ]

t_LOCAL = r'^(_|[a-z])[a-zA-Z0-9_]*'
t_GLOBAL = r'\$[a-zA-Z][a-zA-Z0-9_]*'
t_CONSTANTS = r'^[A-Z][A-Z0-9_]*'
t_INSTANCEVAR = r'^@[a-zA-Z][a-zA-Z0-9_]*'
t_CLASSVAR = r'^@@[a-zA-Z][a-zA-Z0-9_]*'
t_PSEUDO = r'self|true|false|nil|__FILE__|__LINE__'

def t_error(token):
    salida = "\ntype:" + token.type
    salida += "\nvalue:" + str(token.value)
    salida += "\nline:" + str(token.lineno)
    salida += "\nposition:" + str(token.lexpos)
    print (salida)
    token.lexer.skip(1)

lex.lex()


texter = ['CONSTANTE', '4local','_local', '$global','@instance', '@@clase_', '@peso',"self",'4']

for i in texter:
    lex.input(i)
    token = lex.token()
    while token is not None:
        print(token.type)
        token = lex.token()

