def post_eval(str):
    stack= []
    for i in str:
        if i.isdigit():
            stack.append(int(i))
        elif i== "+":
            dig1= stack.pop()
            dig2= stack.pop()
            stack.append(int(dig1)+ int(dig2))
        elif i== "-":
            dig1= stack.pop()
            dig2= stack.pop()
            stack.append(int(dig1)- int(dig2))
        elif i== "/":
            dig1= stack.pop()
            dig2= stack.pop()
            stack.append(int(dig1)/ int(dig2))
        elif i== "*":
            dig1= stack.pop()
            dig2= stack.pop()
            stack.append(int(dig1)* int(dig2))
        else:
            return "Invalid"    
    return stack.pop()
