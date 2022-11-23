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


def student_score_view(_lenName):
    lesName = _lenName
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


def score_view():
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


def student_pass_rate(_lenName):
    lesName = _lenName
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


def less_view(_lessName):
    sqlcmdAvg = "SELECT lessoninfo.lesName,AVG( score )" \
                "FROM stchoose,lessoninfo " \
                "WHERE lessoninfo.lesNo = stchoose.lesNo " \
                "AND lessoninfo.lesName = '%s'" \
                "GROUP BY	lessoninfo.lesNo" % _lessName
    sqlcmdall = "SELECT studentinfo.StudentNo, studentinfo.`Name`,lessoninfo.lesName,score " \
                "FROM stchoose, studentinfo, lessoninfo " \
                "WHERE studentinfo.StudentNo = stchoose.StudentNo " \
                "AND lessoninfo.lesName = '%s'" \
                "AND stchoose.lesNo = lessoninfo.lesNo" % _lessName
    cur.execute(sqlcmdall)
    tempall = cur.fetchall()
    cur.execute(sqlcmdAvg)
    tempAvg = cur.fetchall()
    print(tempAvg)
    print(tempall)

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

    maxSocre = find_socre_max(tempall, _lessName)
    minSocre = find_socre_min(tempall, _lessName)
    pyplot.title('%s课程平均分' % _lessName)
    pyplot.ylabel('分数')
    pyplot.bar("平均分", tempAvg[0][1])
    pyplot.bar("最高分", maxSocre)
    pyplot.bar("最低分", minSocre)
    pyplot.text("平均分", tempAvg[0][1], "%.2f" % tempAvg[0][1], ha='center', va='bottom', fontsize=10)
    pyplot.text("最高分", maxSocre, maxSocre, ha='center', va='bottom', fontsize=10)
    pyplot.text("最低分", minSocre, minSocre, ha='center', va='bottom', fontsize=10)

    pyplot.show()
"""
_lessName = "Math"
sqlcmdAvg = "SELECT lessoninfo.lesName,AVG( score )" \
            "FROM stchoose,lessoninfo " \
            "WHERE lessoninfo.lesNo = stchoose.lesNo " \
            "AND lessoninfo.lesName = '%s'" \
            "GROUP BY	lessoninfo.lesNo" % _lessName
sqlcmdall = "SELECT studentinfo.StudentNo, studentinfo.`Name`,lessoninfo.lesName,score " \
            "FROM stchoose, studentinfo, lessoninfo " \
            "WHERE studentinfo.StudentNo = stchoose.StudentNo " \
            "AND lessoninfo.lesName = '%s'" \
            "AND stchoose.lesNo = lessoninfo.lesNo" % _lessName
cur.execute(sqlcmdall)
tempall = cur.fetchall()
cur.execute(sqlcmdAvg)
tempAvg = cur.fetchall()
print(tempAvg)
print(tempall)


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


maxSocre = find_socre_max(tempall, _lessName)
minSocre = find_socre_min(tempall, _lessName)
pyplot.title('课程平均分')
pyplot.xlabel('课程名')
pyplot.ylabel('分数')
pyplot.bar("平均分", tempAvg[0][1])
pyplot.bar("最高分", maxSocre)
pyplot.bar("最低分", minSocre)
pyplot.text("平均分", tempAvg[0][1], "%.2f" % tempAvg[0][1], ha='center', va='bottom', fontsize=10)
pyplot.text("最高分", maxSocre, maxSocre, ha='center', va='bottom', fontsize=10)
pyplot.text("最低分", minSocre, minSocre, ha='center', va='bottom', fontsize=10)

pyplot.show()
"""
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
