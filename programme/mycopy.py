# 练习:
#   1. 写程序,实现文件的复制,(注:只复制文件,不复制文件夹)
#     要求:
#       1) 要考虑文件关闭的问题
#       2) 要考虑超大文件无法一下加载到内存的问题
#       3) 要能复制二进制文件(非文本文件)

def copy(src_file, dst_file):
    '''  src_file : 源文件名
         dst_file : 目标文件名
         返回值: True成功, False 失败
    '''
    try:
        fr = open(src_file, 'rb')
        try:
            fw = open(dst_file, 'wb')
            try:
                while True:
                    b = fr.read(4096)
                    if not b:
                        break
                    fw.write(b)
            finally:
                fw.close()
        finally:
            fr.close()
    except OSError:
        return False
    return True

src = input("请输入源文件名: ")
dst = input("请输入目标文件名: ")
if copy(src, dst):
    print("复制文件成功!")
else:
    print("复制文件失败!")