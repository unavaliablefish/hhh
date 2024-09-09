a=True
dict1={}
while a:
    newdict={v:k for k,v in dict1.items()}
    print('请输入功能：')
    print(' 1:输入\n','2:查找\n','3:退出\n')
    b=input("请输入你想要的操作：")
    if b=='1':
        en=input("请输入英文单词（按回车结束）：")
        ch=input('请输入中文翻译：')
        dict1.update({en:ch})
        print('该单词已添加到字典库。')
    elif b=='2':
        c=input('请输入要查询的内容（按回车结束）：')
        if c in dict1.keys():
            print(c,"的中文翻译是",dict1[c])
        elif c in dict1.values():
            print(c,'的英文是',newdict[c])
        else:
            print('库中无此单词')
    elif b=='3':
        a=False
    else:
        print('请输入正确指令')
        