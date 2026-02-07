from extraction_element import extraction
from evaluation import expression_eval

user_input = (input("Enter the input: ")).replace(" ","")
expression_list = extraction(user_input)
print(expression_list)

result = ( expression_eval(expression_list) )[0]
print(result)