#Infix Converter

from stack import Stack

class InfixConverter:
        def __init__(self):
            self.stack = Stack()

        def convert_infix(self, infix_expression):
            #Reset the stack for each conversion
            self.stack = Stack() 
            #Create an empty list to hold the characters of the converted postfix expression
            converted_postfix_expression = []

            #Split the infix expression into characters and iterate through them
            characters = infix_expression.split()
            
            for character in characters:
                #If the character is a letter or number, append it into the list
                if character.isalnum():
                    converted_postfix_expression.append(character)

                #if the character is a left parenthesis, push it onto the stack
                elif character == '(':
                    self.stack.push(character)

                #If the character is a right parenthesis, add all characters to the stack until the left parenthesis is reached, and then pop the left parenthesis from the stack
                elif character == ')':
                    while (not self.stack.is_empty() and self.stack.peek() != '('):
                        converted_postfix_expression.append(self.stack.pop())
                    #Pop the left parenthesis from the stack
                    self.stack.pop()  

                #In any other case, the character is an operator, so pop all operators from the stack that have higher or equal precedence and append them to the list, then push the current operator onto the stack
                else:
                    #While the stack is not empty and the precedence of the operator at the top of the stack is greater than or equal to the precedence of the current operator, pop the operator from the stack and append it to the list
                    while (not self.stack.is_empty() and self.stack.peek() != '('):
                        character_at_top_of_stack = self.stack.peek()
                        #if the operator at the top of the stack has higher precedence than the current operator, pop it from the stack and append it to the list
                        if character_at_top_of_stack in ['*', '/'] and character in ['+', '-']:
                            converted_postfix_expression.append(self.stack.pop())

                        #If the operator at the top of the stack has equal precedence to the current operator, pop it from the stack and append it to the list
                        elif character_at_top_of_stack in ['*', '/'] and character in ['*', '/']:
                            converted_postfix_expression.append(self.stack.pop())

                        elif character_at_top_of_stack in ['+', '-'] and character in ['+', '-']:
                            converted_postfix_expression.append(self.stack.pop())

                        #For any other case, the operator at the top of the stack has lower precedence than the current operator, so break out of the loop
                        else:
                            break
                    #The current operator has lower precedence than the operator at the top of the stack, so push the current operator onto the stack
                    self.stack.push(character) 

            while not self.stack.is_empty():
                    converted_postfix_expression.append(self.stack.pop())

            return " ".join(converted_postfix_expression)