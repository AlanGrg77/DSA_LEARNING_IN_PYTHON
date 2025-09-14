import ctypes 

class My_array:
    def __init__(self):
        self.size = 1
        self.n = 0

        self.A = self.__make_array(self.size)
    
    def __len(self):
        return self.n
    
    
    
    def __make_array(self, capacity):
        return (capacity * ctypes.py_object)()

L = My_array()
print(L)