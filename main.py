def push(stack, data, max_length):
    if len(stack) < max_length:
        stack.append(data)
    else:
        print("over flow")

    return stack

def pop(stack):
    if len(stack) > 0:
        del(stack[4 - choice_pop])
    else:
        print("under flow")

max_length = 3
stack = []
choice_pop = 0
while True:

    que = input("Enter push or pop : ")

    if que == "push":
        data = int(input("Enter the number : "))
        stack = push(stack, data, max_length)

    elif que == "pop":
        stack = pop(stack)
        choice_pop += 1