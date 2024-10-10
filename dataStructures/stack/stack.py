from sys import maxsize

class Stack:
    # Function to create a stack. It initializes size of stack as 0
    def __init__(self):
        self.stack = []
    
    # Stack is empty when stack size is 0
    def isEmpty(self, stack):
        return print(f'Is the stack empty: {len(self.stack) == 0}')
    
    # Function to add an item to stack. It increases size by 1
    def push(self, item):
        self.stack.append(item)
        print(f'def push: {item} +  Pushed to stack.')

    # Function to remove an item from stack. It decreases size by 1
    def pop(self, stack):
        if (self.isEmpty(stack)):
            return (str(-maxsize -1), print(f"{stack} nothing in stack")) # return minus infinite
        return print(f'Pop from stack: {self.stack.pop()}')
    

    # Function to return the top from stack without removing it
    def peek(self, stack):
        if (self.isEmpty(stack)):
            return str(-maxsize -1)
        return print(f'Value of the stack peek element is: {self.stack[len(self.stack) -1]}')
