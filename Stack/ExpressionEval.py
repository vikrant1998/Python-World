# Python program to convert infix expression to postfix 
  
# Class to convert the expression 
class Conversion: 
      
    # Constructor to initialize the class variables 
    def __init__(self, capacity): 
        self.top = -1 
        self.capacity = capacity 
        # This array is used a stack  
        self.array = [] 
        # Precedence setting 
        self.output = [] 
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3} 
      
    # check if the stack is empty 
    def isEmpty(self): 
        return True if self.top == -1 else False
      
    # Return the value of the top of the stack 
    def peek(self): 
        return self.array[-1] 
      
    # Pop the element from the stack 
    def pop(self): 
        if not self.isEmpty(): 
            self.top -= 1
            return self.array.pop() 
        else: 
            return "$"
      
    # Push the element to the stack 
    def push(self, op): 
        self.top += 1
        self.array.append(op)  
  
    # A utility function to check is the given character 
    # is operand  
    def isOperand(self, ch): 
        return ch.isdigit() 
  
    # Check if the precedence of operator is strictly 
    # less than top of stack or not 
    def notGreater(self, i): 
        try: 
            a = self.precedence[i] 
            b = self.precedence[self.peek()] 
            return True if a  <= b else False
        except KeyError:  
            return False
              
    # The main function that converts given infix expression 
    # to postfix expression 
    def infixToPostfix(self, exp): 
          
        # Iterate over the expression for conversion 
        num = 0
        wasOp = 0
        n = 0
        for i in exp:
            n += 1
            # If the character is an operand,  
            # add it to output 
            if self.isOperand(i):
                num = num*10 + int(i)
                wasOp = 1
                if n != len(exp):
                    continue
            
            if wasOp == 1:
                self.output.append(str(num)) 
                wasOp = 0
                num = 0

            # If the character is an '(', push it to stack 
            if i  == '(': 
                self.push(i) 
  
            # If the scanned character is an ')', pop and  
            # output from the stack until and '(' is found 
            elif i == ')': 
                while( (not self.isEmpty()) and self.peek() != '('): 
                    a = self.pop() 
                    self.output.append(a) 
                if (not self.isEmpty() and self.peek() != '('): 
                    return -1
                else: 
                    self.pop() 
  
            # An operator is encountered 
            elif i in self.precedence.keys(): 
                while(not self.isEmpty() and self.notGreater(i)): 
                    self.output.append(self.pop()) 
                self.push(i) 

        # pop all the operator from the stack 
        while not self.isEmpty(): 
            self.output.append(self.pop()) 
  
        return self.output

def Result(val1, val2, op):
    if op == '*': return val1 * val2
    elif op == '/': return val1 / val2
    elif op == '+': return val1 + val2
    elif op == '-': return val1 - val2
    elif op == '^': return val1 ^ val2

def evaluateExpression(postfix):
    myStack = []
    for val in postfix:
        if val.isdigit():
            myStack.append(int(val))
        else:
            val1 = myStack.pop()
            val2 = myStack.pop()
            myStack.append(Result(val2, val1, val))

    print(myStack)

if __name__ == "__main__":
    # Driver program to test above function 
    exp = "16+2/3*(4+5)-9"
    exp = ''.join(exp.split(' '))
    obj = Conversion(len(exp)) 
    postfix = obj.infixToPostfix(exp)
    evaluateExpression(postfix)