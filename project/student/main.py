'''主调用模块

此模块会调用menu,student_info两个模块'''

from menu import menu
from student_info import *

def face ():
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
        elif a=='9':
            infos=myfile()
        elif a=='10':
            save(infos)
        elif a=='q':
            print('程序结束')
            break
face()