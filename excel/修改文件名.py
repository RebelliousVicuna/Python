import os
#修改文件名：
path=input("请输入要更改的目标文件夹的 文件路径：（末尾加上\\)\n")
filelist=os.listdir(path)
print(list(filelist))
ans=input("该目录是否为需要修改的文件：（输入y 或者 n)\n")
if ans=='n':
    print("重新运行该程序")
    exit()
else: print("继续\n")
mubiaofile=[]
x=['555','6667','qqqsxq']
for filename in filelist:
    pos=os.path.splitext(filename)  #拆分文件名=文件名称+后缀名称 使用pos列表储存
    if pos[1]=='.pdf' :             #目标文件的后缀
       mubiaofile.append(str(filename))     #获得所有目标文件
# print(mubiaofile[0])
for i in range(len(mubiaofile)) :
    oldname=path+os.sep+mubiaofile[i]   # os.sep 添加系统分隔符
    newname=path+os.sep+x[i+1]+'.pdf'
    os.rename(oldname,newname)
    print(newname)