from compiler.ast import StmtNode

class ReturnNode(StmtNode):
    expr = None
    
    def __init__(self, loc, expr):
        super().__init__(loc)
        self.expr = expr
    def accept(self, visitor):
        return visitor.visit(self)
