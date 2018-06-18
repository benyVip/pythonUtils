
#coding=utf-8

#添加文末的后缀
f = open("a.txt")
w = open("b.txt",'w')

orderSnList = f.readlines();
updateSql = "select * from table where order_sn in ( "
for orderSn in orderSnList:
      updateSql+='\''+orderSn+'\''+','

updateSql = updateSql[:-1];
updateSql+=")"

print "成功"
w.write(updateSql)



