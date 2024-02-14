inp = input("Введите скобочную последовательность: ")

def clear(data):
    allowed = ["{", "(", "[", "<", "}", ")", "]", ">"]
    cleared = ""
    for i in data:
        if i in allowed:
            cleared += i
    return cleared

def check_brackets(data):
    stack = [] 
    res = None

    for i in data: 
        if i in ["{", "(", "[", "<"]: 
            stack.append(i) 
        else: 
            if stack == []: 
                return False
            cur_char = stack.pop() 
            if cur_char == '{': 
                if i != "}": 
                    return False
            if cur_char == '(': 
                if i != ")": 
                    return False
            if cur_char == '[': 
                if i != "]": 
                    return False
            if cur_char == '<': 
                if i != ">": 
                    return False
                    
    
    if stack != []: 
        res = False
    else:
        res = True
    return res

r = clear(inp)
r = check_brackets(r)
print(r)
