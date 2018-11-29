class AST(object):
    """
    Clase base para AST
    """
    _fields = []
    def __init__(self,*args,**kwargs):
        assert len(args) == len(self._fields)
        for name,value in zip(self._fields,args):
            setattr(self,name,value)
        # agregando keys
        for name,value in kwargs.items():
            setattr(self,name,value)
    
    def visit(self,node):
        """
        Metodo de forma visit_metodo(node), "metodo" es el nombre
        del nodo en particular
        """
        if node:
            method = "visit_" + node.__class__.__name__
            visitor = getattr(self, method, self.generic_visit)
            return visitor(node)
        else:
            return None
    
    def generic_visit(self,node):
        """
        Examina si el nodo tiene mas elementos en _fields
        """
        for field in getattr(node,"_fields"):
            value = getattr(node,field,None)
            if isinstance(value, list):
                for item in value:
                    if isinstance(item,AST):
                        self.visit(item)
            elif isinstance(value, AST):
                self.visit(value)

class Assign(AST):
    _fields = ["variable", "op", "valor"]

class Math(AST):
    _fields = ["terminoder", "op", "terminoizq"]

class SexprAST(AST):
    _fields = ["sterm", "op", "sterm"]

class Logical(AST):
    _fields = ["first_term", "comparator", "second_term"]

class IfAST(AST):
    _fields = ["first_term", "second_term", "third_term", "fourth_term", "end"]

class IfAST_f(AST):
    _fields = ["if", "logic", "then", "expr", "end"]

class IfAST_t(AST):
    _fields = ["if", "logic", "then"]

class IfAST_d(AST):
    _fields = ["if", "else"]

class ElseAST(AST):
    _fields = ["else","expr", "salto"]

class ElseifAST(AST):
    _fields = ["first_term", "second_term", "third_term", "end"]

class ElseifAST_t(AST):
    _fields = ["first_term", "second_term", "end"]

class WhileAST(AST):
    _fields = ["while", "logic", "salto", "code", "salto", "end"]

class WhileAST_s(AST):
    _fields = ["while", "logic", "salto", "code", "salto"]

class WhileAST_c(AST):
    _fields = ["while", "logic", "salto", "code"]

class IteratorAST(AST):
    _fields = ["termino", "puntos", "termino"]

class ExpAST(AST):
    _fields = ["termino","puntos","termino"]

class ForAST(AST):
    _fields = ["for", "iterator", "in", "expr", "code","end"]

class ForAST_o(AST):
    _fields = ["for", "iterator", "in", "expr", "do","code", "end"]

class FinalAST(AST):
    _fields = ["Then","expr"]

class CodeAST(AST):
    _fields = ["code","code"]

class ArrayAST(AST):
    _fields = ["elemento","coma","elemento"]

class AsArrayAST(AST):
    _fields = ["var","ass","array"]

class IndexAST(AST):
    _fields = ["var", "brack","valor","brack"]

class SlideAST(AST):
    _fields = ["var", "brack","slide","brack"]   

class DefSlideAST(AST):
    _fields = ["int", "double", "int"]

class NumberAST(AST):
    _fields = ["number"]

class StringAST(AST):
    _fields = ["string"]