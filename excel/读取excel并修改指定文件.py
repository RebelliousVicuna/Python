import xlrd,os
filename=input("请输入目标excel文件路径:\n")
workbook=xlrd.open_workbook(filename)
# 获取所有sheet
# AllNames=workbook.sheet_names()     #所有表对象

# print(AllNames) #['xx', 'XX']  输出所有的表名，以列表的形式

# 根据sheet索引或者名称获取sheet内容

# print(sheet)    #打印其属性
name = input("请输入sheet表序号:\n")
worksheet = workbook.sheet_by_index(int(name)-1)  # 索引选择对象,获得 表 对象，
# worksheet = workbook.sheet_by_name(name)     #通过表名称获得对象
# sheet0_name = workbook.sheet_names()[0]  #通过sheet索引获取sheet名称

# print(sheet0_name)  #  “学生表”
# name=worksheet.name  #获取表的姓名print(name) #各省市
# nrows=worksheet.nrows  #获取该表总行数
# print(nrows)  # 14
# ncols=worksheet.ncols  #获取该表总列数
# print(ncols) # 3

# for i in range(nrows):                  #循环打印每一行
#     print(worksheet.row_values(i))
# for i in range (ncols):                 #循环打印每一列
#     print(worksheet.col_values(i))
sum=input("需要选择几列：\n")
b=[]
templist=[]
for i in range(int(sum)) :

    temp= input("请输入你要选择的列：(一次输入一个数字，按一次回车)\n")
    b.append(int(temp))
    # print(b[i])
    templist.append(worksheet.col_values(int(b[i])-1))
    # print(worksheet.col_values())
    print(worksheet.col_values(int(b[i])-1))
# print(worksheet.cell_value(0,1))      #获取特定单元格cell（x，y）

for i in range(int(sum)-1):
    # temp_a=templist[i]
    # temp_b=templist[i+1]
    templist[0] = list(zip(templist[0], templist[i+1]))     #对应打包成元组

temp_num=[]
for i in range(len(templist[0])):
    # 获取合并列中的每一组元素，并剔除特定字符,追加到 temp_num列表中
    temp_num.append(str(templist[0][i]).replace(' ','').replace('.0','').replace(',','').replace('(','').replace(')','').replace("'",""))
for i in range(len(templist[0])):
    print(temp_num[i])

ans=input("生成的文件名是否是正确的文件名（y or n?)\n")
if ans=='n':
    exit()
else:
    print("继续\n")
# 目标字符串列表 ：temp_num

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
houzhui=input("请输入要更改文件的后缀格式:\n")
for filename in filelist:
    pos=os.path.splitext(filename)  #拆分文件名=文件名称+后缀名称 使用pos列表储存
    if pos[1]=='.'+houzhui :             #目标文件的后缀
       mubiaofile.append(str(filename))     #获得所有目标文件
# print(mubiaofile[0])
for i in range(len(mubiaofile)) :
    oldname=path+os.sep+mubiaofile[i]   # os.sep 添加系统分隔符
    newname=path+os.sep+temp_num[i+1]+'.'+houzhui

    os.rename(oldname, newname)
    print(temp_num[i+1]+'.'+houzhui)
print("修改完成")

input("输入任意字符退出")