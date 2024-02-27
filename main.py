import art

print(art.logo)

def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

operations ={
  "+": add,
  "-":subtract,
  "/":divide,  
  "*":multiply
} 
def calculator():
  num1 = float(input("What is the first number? "))
  gaming = True
  while  gaming:
    num2 = float(input(f"What is the second number? "))
    operation_symbol = input("select the operation you wish to use : ")  
    answer = None
  
    answer = operations[operation_symbol](num1,num2)
  
    if answer is not None:
      print(f"{num1} {operation_symbol} {num2} = {answer}")
    else:
      print("Operation not found")
  
    answer_input = input("Type 'y' to continue calculating or n to exit: ")
    if answer_input == "y":
        num1 = answer
  
    else:
      gaming = False
      print("Good bye buddy!!")

calculator()
