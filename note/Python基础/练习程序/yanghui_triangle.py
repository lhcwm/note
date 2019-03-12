# 　4. 打印杨辉三角，只打印6层
#        1
#       1 1
#      1 2 1
#     1 3 3 1
#    1 4 6 4 1
#  1 5 10 10 5 1

def get_next_line(L):
    L2 = [1]
    for i in range(len(L)-1):
        L2.append(L[i] + L[i+1])
    L2.append(1)
    return L2


def get_yangui_list(n):
    L = []
    layer = [1]
    while len(L) < n:
        L.append(layer)
        layer = get_next_line(layer)  # 算出下一层
    return L


def get_yangui_string_list(L):
    L2 = []
    for layer in L:
        s = ' '.join((str(x) for x in layer))
        L2.append(s)
    return L2

def print_yanghui_triangle(L):
    max_len = len(L[-1])
    for s in L:
        print(s.center(max_len))

L = get_yangui_list(10)
string_L = get_yangui_string_list(L)
print_yanghui_triangle(string_L)







