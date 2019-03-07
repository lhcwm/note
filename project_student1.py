
def chinese_char_count(s):
    l=[]
    k=0
    for n in s:
        for a in n['name']:
            if 0x4E00<=ord(a)<=0x9FA5:
                k+=1
            l+=[k]
    return max(l)

def input_student():
    l=[]
    while 1:
        a=input('请输入姓名：')
        if a =='':
            break
        b=input('请输入年龄：')
        c=input('请输入成绩：')
        d={'name':a,'age':b,'score':c}
        l.append(d)
    return l




def output_student(Ｌ):
    print('+'+('-'*(k+6))+'+'+('-'*8)+'+'+('-'*8)+'+')
    print('|'+'姓名'.center(k+4)+'|'+'年龄'.center(6)+'|'+'成绩'.center(6)+'|')
    print('+'+('-'*(k+6))+'+'+('-'*8)+'+'+('-'*8)+'+')
    for x in L:
        m=0
        for a in x['name']:
            if 0x4E00<=ord(a)<=0x9FA5:
                m+=1
                # break
        print('|%s|%s|%s|'%(x['name'].center((k+6-m),x['age'].center(8),x['score'].center(8))))
        # print('|'+x['name'].center((k+6-m))+'|'+x['age'].center(8)+'|'+x['score'].center(8)+'|')
    print('+'+('-'*(k+6))+'+'+('-'*8)+'+'+('-'*8)+'+')


infos=input_student()
k=chinese_char_count(infos)
print (infos)
output_student(infos)
