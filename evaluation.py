def expression_eval(expression_list):

    for i in ["/","*","+","-"]:

        if i in expression_list:
            index_operator = expression_list.index(i)

            if i == "/":
                result = [expression_list[index_operator-1] / expression_list[index_operator+1]]
                expression_list = expression_list[:index_operator-1] + result + expression_list[index_operator+2:]

                if i in expression_list:
                    return expression_eval(expression_list)
                
            elif i == "*":
                result = [expression_list[index_operator-1] * expression_list[index_operator+1]]
                expression_list = expression_list[:index_operator-1] + result + expression_list[index_operator+2:]

                if i in expression_list:
                    return expression_eval(expression_list)
                
            elif i == "+":
                sign = "+"

                if expression_list[index_operator-2] == "-":
                    result = [- expression_list[index_operator-1] + expression_list[index_operator+1]]
                    if result[0] <0:
                        sign = "-"
                        result = result[1:]
                    expression_list = expression_list[:index_operator-2] + [sign] + result + expression_list[index_operator+2:]

                else:
                    result = [expression_list[index_operator-1] + expression_list[index_operator+1]]
                    expression_list = expression_list[:index_operator-1] + result + expression_list[index_operator+2:]

                if i in expression_list:
                    return expression_eval(expression_list)
                
            elif i == "-":
                result = [expression_list[index_operator-1] - expression_list[index_operator+1]]
                expression_list = expression_list[:index_operator-1] + result + expression_list[index_operator+2:]

                if i in expression_list:
                    return expression_eval(expression_list)
            else:
                pass

    return expression_list