#Infix and Postfix Expressions Project Test Program

import postfix_evaluator
from stack import Stack
from postfix_evaluator import PostfixEvaluator
from infix_converter import InfixConverter

#Test Data for Postfix Evaluation from Canvas:
postfix = ["5 3 +",
           "8 2 - 3 +",
           "5 3 8 * +",
           "6 2 / 3 +",
           "5 8 + 3 -",
           "5 3 + 8 *",
           "8 2 3 * + 6 -",
           "5 3 8 * + 2 /",
           "8 2 + 3 6 * -",
           "5 3 + 8 2 / -"]


print("----- Postfix Evaluator -----")
postfix_evaluator = PostfixEvaluator()
for expression in postfix:
    expression_evaluated = postfix_evaluator.evaluate_postfix(expression)
    print(f"{expression} = {expression_evaluated}")