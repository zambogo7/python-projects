# A program to create a calculator
#add function
def add(n1,n2):
    return n1+n2

#sub function
def sub(n1,n2):
    return n1-n2

#mult function
def mult(n1,n2):
    return n1*n2

#div function
def div(n1,n2):
    return n1/n2
# dictionary
opperations={
    "+":add,
    "-":sub,
    "*":mult,
    "/":div
}
def calculator():
    should_continue=True
    while should_continue:
        n1=int(input("Enter First number: "))
        symbol=input("Enter a symbol for your operation '+' '-' '*' '/': ")
        n2=int(input("Enter second number: " ))
        for operation,fantion in opperations.items():
            if symbol==operation in opperations:
                answer=fantion(n1,n2)
                print(f"{n1}{symbol}{n2}={answer}")

        if input("Enter 'y' to perfom another operation or 'n' to exit: ").lower()=="y":
            n1=answer
        else:
            should_continue=False
            calculator()
calculator()
    


