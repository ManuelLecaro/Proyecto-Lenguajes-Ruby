class Nodo:
    def __init__(self, data):
        self.left = None
        self.rigth = None
        self.data = data
        self.priority = 0
    
    def print_Tree(self):
        print(self.data)
    
    def insertNode(self, priority, data):
        """
        Insert new node with data

        @param data node data object to insert
        """
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Nodo(data)
                else:
                    self.left.insertNode(priority, data)
            elif data > self.data:
                if self.rigth is None:
                    self.rigth = Nodo(data)
                else:
                    self.rigth.insertNode(priority, data)
        else:
            self.data = data


    def lookup(self, data, parent=None):
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.rigth is None:
                return None, None
            return self.rigth.lookup(data, self)
        else:
            return self, parent


        
        
                


        