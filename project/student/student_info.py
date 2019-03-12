def input_student():
    '''输入学生信息的函数'''
    l=[]
    while 1:
        a=input('请输入姓名：')
        if a =='':
            break
        try:
            b=int(input('请输入年龄：'))
            c=int(input('请输入成绩：'))
        except ValueError:
            print('输入有错,请重新输入')
            continue
        d={'name':a,'age':b,'score':c}
        l.append(d)
    return l


def output_student(Ｌ):
    '''显示学生信息的函数'''
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
              '|'+str(x['age']).center(8)+
              '|'+str(x['score']).center(8)+'|')
    print('+'+('-'*(k+6))+'+'+('-'*8)+'+'+('-'*8)+'+')

def mydel(j):
    '''删除信息的函数'''
    a=input('删除谁的信息')
    for n in j:
        if n['name']==a:
            print('删除',a,'的信息成功')
            j.remove(n)
            break
    print('删除失败')
    return j

def change(i):
    '''修改信息的函数'''
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

def myfile():
    '''从文件读取信息的函数'''
    try:
        s=input('输入文件名')
        f=open(s)
    except FileNotFoundError:
        print('输入的文件名有误')
        return
    y=('name','age','score')
    l=[]
    try:
        while 1:
            x=f.readline()
            if not x:
                break
            x=x.replace('\n','')
            z=x.split(',')
            d=dict(zip(y,z))
            l.append(d)
    finally:
        f.close()
    print('文件信息导入成功')
    return l

def save(l):
    '''保存信息到文件的函数'''
    try:
        a=input('输入要保存的文件名')
        f=open(a,'a')
        for x in l:
            f.writelines([x['name'],',',str(x['age']),',',str(x['score']),'\n'])
        f.close()
        print('保存成功')
    except OSError:
        print('保存失败')
