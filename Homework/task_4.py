n = int(input())
f_names = input().split(' ')
reversed_f_names = list(reversed(f_names))
check = 0
m = int(input())
i = 0
f_dict = {}
result = []
while i < m:
    new_line = input().split(' ')
    if new_line[0] not in f_dict:
        f_dict[new_line[0]] = {new_line[1]: new_line[2]}
    else:
        f_dict[new_line[0]][new_line[1]] = new_line[2]
    i += 1
ex = input()
for el in range(len(reversed_f_names)):
    if reversed_f_names[el] in f_dict:
        for key in f_dict[reversed_f_names[el]]:        
            if key == ex or check == 1:            
                if f_dict[reversed_f_names[el]][key] == '_':
                    result.append(reversed_f_names[el])
                    check = 1
                    break
                elif check == 1:
                    result.append(reversed_f_names[el])
                    break                
                else:
                    ex = f_dict[reversed_f_names[el]][key]
                    break                
            else:
                continue
    else:
        if check == 1:
            result.append(reversed_f_names[el])
        else:
            continue
str_result = ''
reversed_result = list(reversed(result))
for el in reversed_result:
    str_result += el + ' '
print(str_result)
