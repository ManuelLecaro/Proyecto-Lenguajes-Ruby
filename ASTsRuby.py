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

class Logical(AST):
    _fields = ["first_term", "comparator", "second_term"]

class IfAST(AST):
    _fields = ["first_term", "second_term", "third_term", "fourth_term", "end"]

class ElseAST(AST):
    _fields = ["else","salto","expr", "salto"]

class ElseifAST(AST):
    _fields = ["first_term", "second_term", "third_term", "fourth_term", "end"]

class WhileAST(AST):
    _fields = ["while", "logic", "salto", "code", "salto", "end"]

class IteratorAST(AST):
    _fields = ["termino", "puntos", "termino"]

class ExpAST(AST):
    _fields = ["termino","puntos","termino"]

class ForAST(AST):
    _fields = ["for", "iterator", "in", "expr", "salto", "code", "salto","end"]

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