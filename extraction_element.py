def extraction (user_input):

    expression_list = []
    current_ele = ""
    length = len(user_input)

    for i in range(length):
        element = user_input[i]

        if element.isdigit() or element == ".":
            current_ele += element
        else:
            if current_ele != "":
                expression_list.append(float(current_ele))
            expression_list.append(element)
            current_ele = ""

        if i == length-1:
            expression_list.append(float(current_ele))

    if expression_list[0] == "-":
        expression_list.insert(0,0)

    return expression_list