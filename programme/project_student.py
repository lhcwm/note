# ３，学生信息管理项目

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
    def chinese_char_count(s):
        l=[]
        for n in s:
            for a in n['name']:
                k=len(n['name'])
                if 0x4E00<=ord(a)<=0x9FA5:
                    k+=1
                l+=[k]
        return max(l)
    k=chinese_char_count(L)
    print('+'+('-'*(k+6))+'+'+('-'*8)+'+'+('-'*8)+'+')
    print('|'+'姓名'.center(k+4)+'|'+'年龄'.center(6)+'|'+'成绩'.center(6)+'|')
    print('+'+('-'*(k+6))+'+'+('-'*8)+'+'+('-'*8)+'+')
    for x in L:
        m=0
        for a in x['name']:
            if 0x4E00<=ord(a)<=0x9FA5:
                m+=1
        print('|'+x['name'].center((k+6-m))+
              '|'+x['age'].center(8)+
              '|'+x['score'].center(8)+'|')
    print('+'+('-'*(k+6))+'+'+('-'*8)+'+'+('-'*8)+'+')

def mydel(j):
    a=input('删除谁的信息')
    for n in j:
        if n['name']==a:
            print('删除',a,'的信息成功')
            j.remove(n)
            break
    print('删除失败')
    return j

def change(i):
    a=input('选择修改谁的信息：')
    print('　1)姓名')
    print('　2)年龄')
    print('　3)成绩')
    b=input('请选择要修改的项：')
    c=input('请输入正确的内容：')
    for n in i:
        if n['name']==a:
            if b=='1':
                n['name']=c
            elif b=='2':
                n['age']=c
            elif b=='3':
                n['score']=c
            print('修改成功')
            break
    print('修改失败')

def menu():
    print('＋－－－－－－－－－－－－－－－－－－－－－＋')
    print('｜　1)添加学生信息　　　　　　　　　　　　　｜')
    print('｜　2)显示学生信息　　　　　　　　　　　　　｜')
    print('｜　3)删除学生信息　　　　　　　　　　　　　｜')
    print('｜　4)修改学生信息　　　　　　　　　　　　　｜')
    print('｜　5)按学生成绩高－低显示学生信息　　　　　｜')
    print('｜　6)按学生成绩低－高显示学生信息　　　　　｜')
    print('｜　7)按学生年龄高－低显示学生信息　　　　　｜')
    print('｜　8)按学生年龄低－高显示学生信息　　　　　｜')
    print('｜　q)退出　　　　　　　　　　　　　　　　　｜')
    print('＋－－－－－－－－　－－－－－－－－－－－－＋')


def face ():
    # infos=[]
    while True:
        menu()
        a=input('请选择')
        if a =='1':
            infos=input_student()
        elif a=='2':
            output_student(infos)
        elif a=='3':
            mydel(infos)
        elif a=='4':
            change(infos)
        elif a=='5':
            infos=sorted(infos,key=lambda x:int(x['score']),reverse=True)
            output_student(infos)
        elif a=='6':
            infos=sorted(infos,key=lambda x:int(x['score']))
            output_student(infos)
        elif a=='7':
            infos=sorted(infos,key=lambda x:int(x['age']),reverse=True)
            output_student(infos)
        elif a=='8':
            infos=sorted(infos,key=lambda x:int(x['age']))
            output_student(infos)
        elif a=='q':
            print('程序结束')
            break
face()

