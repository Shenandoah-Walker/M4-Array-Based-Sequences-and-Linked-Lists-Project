#Postfix Evaluator

from stack import Stack

class PostfixEvaluator:

    def __init__(self):
        self.stack = Stack()

    def evaluate_postfix(self, postfix_expression):
        #Reset the stack for each evaluation
        self.stack = Stack()  

        characters = postfix_expression.split()

        for character in characters:
            #If the character is a number, push it onto the stack
            if character.isdigit(): 
                self.stack.push(int(character))
            #In any other case, the character is an operator, so pop the top two operands, apply the operator, and push the result back onto the stack
            else:  
                right_number = self.stack.pop()  
                left_number = self.stack.pop()

                #Determine which 
                if character == '+':
                    self.stack.push(left_number + right_number)

                elif character == '-':
                    self.stack.push(left_number - right_number)

                elif character == '*':
                    self.stack.push(left_number * right_number)

                elif character == '/':
                    self.stack.push(left_number / right_number)

                else:
                    raise ValueError(f"The following operator is not basic arithmetic and therefore cannot be evaluated: {character}")

            return self.stack.pop()

    