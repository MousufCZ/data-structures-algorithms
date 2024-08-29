from dataStructures import stack

dsInstance = stack.Stack()
currentStack = dsInstance.stack

dsInstance.isEmpty(currentStack)

dsInstance.push(1)
dsInstance.push(2)
dsInstance.push(3)
dsInstance.push(4)

dsInstance.isEmpty(currentStack)
print(currentStack)

dsInstance.pop(currentStack)
print(currentStack)

dsInstance.peek(currentStack)

if __name__ == "__main__":
        print(f"Data structures: Current stack is {currentStack} ....")