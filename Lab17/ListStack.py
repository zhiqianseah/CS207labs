from StackInterface import StackInterface 

#your code here
class ListStack(StackInterface):
    
    def __init__(self):
        self._list = []
        
    def push(self, value):    
        self._list.append(value)
        
    def pop(self):
        if len(self._list) == 0:
            return None
        return self._list.pop()
        
    def peek(self):
        if len(self._list) == 0:
            return None
        temp = self._list.pop()
        self._list.append(temp)
        return temp