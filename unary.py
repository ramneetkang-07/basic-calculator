def unary_simplify(user_input):
    expression=[user_input[0]]
    pls_cnt = 0
    minus_cnt = 0

    for i in range(1,len(user_input)):
        ele = user_input[i]

        if ele in ["+","-"]:
            if ele == "+":
                pls_cnt+=1
            elif ele == "-":
                minus_cnt+=1
        
        elif isinstance(ele,float):

            if expression[-1] not in ["/", "*"]:
                expression.append("+")
                
            if minus_cnt % 2 != 0:
                expression.append(float(-ele))
            else:
                expression.append(ele)
            
            pls_cnt = 0
            minus_cnt = 0

        elif ele in ["/","*"]:
            expression.append(ele)
            
    return expression