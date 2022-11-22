import numpy
from matplotlib import pyplot
import ConnectDatabase

pyplot.rcParams['font.sans-serif'] = ['SimHei']
pyplot.rcParams['axes.unicode_minus'] = False

# 建立数据库连接
condaba = ConnectDatabase.ConData(_host='127.0.0.1',
                                  _db='student2022',
                                  _port=3306,
                                  _user='root',
                                  _password='root',
                                  _charset='utf8')
# 获取数据库连接
conn = condaba.get_con_database()
cur = conn.cursor()
"""
lesName = "Math"
sqlcmdallok = "SELECT studentinfo.StudentNo, studentinfo.`Name`,lessoninfo.lesName,score " \
              "FROM stchoose, studentinfo, lessoninfo " \
              "WHERE studentinfo.StudentNo = stchoose.StudentNo " \
              "AND stchoose.lesNo = lessoninfo.lesNo " \
              "AND stchoose.score >= 60 " \
              "AND lessoninfo.lesName = '%s'" % lesName
sqlcmdall = "SELECT studentinfo.StudentNo, studentinfo.`Name`,lessoninfo.lesName,score " \
            "FROM stchoose, studentinfo, lessoninfo " \
            "WHERE studentinfo.StudentNo = stchoose.StudentNo " \
            "AND stchoose.lesNo = lessoninfo.lesNo " \
            "AND lessoninfo.lesName = '%s'" % lesName
cur.execute(sqlcmdallok)
tempallok = cur.fetchall()
print(tempallok)
print(len(tempallok))
cur.execute(sqlcmdall)
tempall = cur.fetchall()
print(tempall)
print(len(tempall))
langs = ['及格', '不及格']
data = []
data.append(float(len(tempallok)) / float(len(tempall)))
data.append(float(len(tempall) - len(tempallok)) / float(len(tempall)))
pyplot.title("%s课程及格率" % lesName)
pyplot.pie(data, labels=langs, autopct='%1.2f%%')
pyplot.show()
"""
"""
sqlcmdAvg = "SELECT lessoninfo.lesName,AVG( score )" \
            "FROM stchoose,lessoninfo " \
            "WHERE lessoninfo.lesNo = stchoose.lesNo " \
            "GROUP BY	lessoninfo.lesNo"
sqlcmdall = "SELECT studentinfo.StudentNo, studentinfo.`Name`,lessoninfo.lesName,score " \
            "FROM stchoose, studentinfo, lessoninfo " \
            "WHERE studentinfo.StudentNo = stchoose.StudentNo " \
            "AND stchoose.lesNo = lessoninfo.lesNo"
cur.execute(sqlcmdall)
tempall = cur.fetchall()
cur.execute(sqlcmdAvg)
tempAvg = cur.fetchall()
print(tempAvg)


def find_socre_max(data, lessName):
    maxSocre = 0.0
    for item in data:
        if item[2] == lessName and item[3] > maxSocre:
            maxSocre = item[3]
    return maxSocre


def find_socre_min(data, lessName):
    minSocre = 1000
    for item in data:
        if item[2] == lessName and item[3] < minSocre:
            minSocre = item[3]
    return minSocre


pyplot.title('课程平均分')
pyplot.xlabel('课程名')
pyplot.ylabel('平均分')
barWidth = 0.25
r1 = numpy.arange(3)
print(r1)
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r_tick = []

for item in zip(tempAvg, r1, r2, r3):
    print(item)
    print(item[1])
    print(item[2])
    print(item[3])
    maxSocre = find_socre_max(tempall, item[0][0])
    minSocre = find_socre_min(tempall, item[0][0])
    r_tick.append(item[0][0])
    pyplot.bar(item[1], item[0][1], width=barWidth)
    pyplot.bar(item[2], maxSocre, width=barWidth)
    pyplot.bar(item[3], minSocre, width=barWidth)
    pyplot.text(item[1], int(item[0][1]), int(item[0][1]), ha='center', va='bottom', fontsize=10)
    pyplot.text(item[2], maxSocre, maxSocre, ha='center', va='bottom', fontsize=10)
    pyplot.text(item[3], minSocre, minSocre, ha='center', va='bottom', fontsize=10)

r_tick_max_min = ["最高分", "最高分", "最高分", "最低分", "最低分", "最低分"]
pyplot.xticks([j for i in [r1, r2, r3] for j in i], [j for i in [r_tick, r_tick_max_min] for j in i])


pyplot.show()

"""
"""
lesName = "Math"
# 用于数据库查询的语句

sqlcmd = "SELECT studentinfo.StudentNo, studentinfo.`Name`,lessoninfo.lesName,score " \
         "FROM stchoose, studentinfo, lessoninfo " \
         "WHERE studentinfo.StudentNo = stchoose.StudentNo " \
         "AND stchoose.lesNo = lessoninfo.lesNo AND lessoninfo.lesName = '%s'" % lesName
cur.execute(sqlcmd)
temp = cur.fetchall()
pyplot.title('%s课程绩分布图' % lesName)
pyplot.xlabel('学号+姓名')
pyplot.ylabel('总分')

for item in temp:
    pyplot.xticks(rotation=90)
    pyplot.bar(item[1] + item[0], item[3])
    pyplot.text(item[1] + item[0], int(item[3]), int(item[3]), ha='center', va='bottom', fontsize=10)

pyplot.show()

"""
