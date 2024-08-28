from sys import maxsize

class Stack:
    # Function to create a stack. It initializes size of stack as 0
    def __init__(self):
        self.stack = []
    
    # Stack is empty when stack size is 0
    def isEmpty(self, stack):
        return len(self.stack) == 0
    
    # Function to add an item to stack. It increases size by 1
    def push(self, item):
        self.stack.append(item)
        print(f"def push: {item} +  Pushed to stack.")

    # Function to remove an item from stack. It decreases size by 1
    def pop(self, stack):
        if (self.isEmpty(stack)):
            return (str(-maxsize -1), print(f"{stack} nothing in stack")) # return minus infinite
        return self.stack.pop()
    
    # Function to return the top from stack without removing it
    def peek(self, stack):
        if (self.isEmpty(stack)):
            return str(-maxsize -1)
        return self.stack[len(self.stack) -1]
    
    def __str__(self):
        return str(self.stack)
    
if __name__ == "__main__":
    stack = Stack()
    print(stack)

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack)

    stack.pop(stack)
    print(stack)

    stack.peek(stack)
    print(stack)