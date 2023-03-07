SIZE = 10
stack = list()
top = -1

def isEmpty():
    return top < 0

def push(val): 
    global top
    top = top + 1
    if (top > SIZE - 1):
        print("Stack is full!")
    else: 
        stack.insert(0, val)

def pop():
    global top
    if (isEmpty()):
        print("Stack is empty")
    else:
        temp = stack[top]
        stack.remove(top)
        top = top - 1

def main(): 
    # pop()
    push(0)
    push(1)
    push(2)
    push(3)
    push(4)
    push(5)
    push(6)
    push(7)
    push(8)
    push(9)
    pop()
    # push(10)
    print("Current stack:")
    for i in stack:
        print(i)


if __name__ =="__main__":
    main()