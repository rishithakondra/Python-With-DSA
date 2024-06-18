#stack using list
class Stack:
    def __init__(self):
        self.items = []
       #4 usages 
    def is_empty(self):
        return len(self.items) == 0
    #3usages
    def push(self,item):
        self.items.append(item)
      #2 usage  
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")
        # 1 usage
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")
    #1 usage
    def size(self):
        return len(self.items)
    
stack=Stack()
print("is the stack empty?",stack.is_empty())
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack:",stack.items)
print("Top of the stack:",stack.peek())
print("pop:",stack.pop())
print("stack after pop:",stack.items)
print("is the stack empty?:",stack.is_empty())
print("Size of the stack:",stack.size())

            
            