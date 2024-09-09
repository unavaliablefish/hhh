vote1 = ['柴进', '卢俊义', '柴进', '柴进', '柴进', '柴进', '卢俊义', '柴进', '弃权',
'卢俊义', '柴进', '柴进', '卢俊义', '柴进', '卢俊义', '卢俊义', '弃权']
vote2 = ['卢俊义', '柴进', '柴进', '董平', '卢俊义', '卢俊义', '柴进', '弃权',
'武松', '史进', '柴进', '卢俊义', '柴进', '林冲', '卢俊义', '弃权', '弃权']
vote3 = ['卢俊义', '柴进', '柴进', '柴进', '卢俊义', '吴用', '林冲', '卢俊义', '柴进', '柴进','弃权', '史进', '吴用', '卢俊义', '柴进', '林冲', '宋江', '宋江', '卢俊义', '弃权', '弃权']
vote4=['鲁智深','弃权','花荣','弃权','林冲','弃权','弃权','史进','吴用','弃权','柴进','弃权','宋江','宋江','卢俊义','弃权','弃权']
vote_all=[vote1,vote2,vote3,vote4]
work=[]
name=[]
sum=0
for i in vote_all:
    for j in i:
        if j!='弃权':
            sum=sum+1
        if j not in name and j!='弃权':
            name.append(j)
        qi=0
        a=len(i)
        b=i.count(j)
        qi=i.count('弃权')
    if qi*3<a:
        work.append(i)
        
print(work)
print(sum)
print(name)
for i in name:
    s=0
    n=0
    for j in vote_all:
        
        if i in j:
            s=s+1
        n+=j.count(i)
        lv=n/sum
    if s>=2 and n>sum*0.35:
        print('晋级名单：{} 得票率:{} 总票数：{}'.format(i,lv,n))
           


        