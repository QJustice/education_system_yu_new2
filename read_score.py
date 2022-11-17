import matplotlib.pyplot as plt
import pandas as pd

#1.在代码开头导入相关的包;




df=pd.read_csv('E:\\student_score.csv',encoding='GBK') #读取student_score.csv文件为DataFrame字符流
#2.在python中读取student_score.csv为DataFrame字符流，并且赋值给df，需要设置编码格式为GBK格式，此处我把student_score.csv文件存放在E盘目录下;


plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False


#3.设置字体格式，下面需要用到matplotlib库，需要设置字体格式，否则图形可视化的时候中文标题无法显示，设置方法如下：




Python_max=df.Python.max() #python最大值
math_max=df.高数.max()  #高数最大值
english_max=df.英语.max()  #英语最大值

Python_min=df.Python.min() #python最小值
math_min=df.高数.min() #高数最小值
english_min=df.英语.min() #英语最小值

name=df.学号
students_scores=df.高数+df.Python+df.英语 #学生总成绩

Python_avg=df.Python.mean()#python平均分
math_avg=df.高数.mean() #高数平均分
english_avg=df.英语.mean() #英语平均分

#4.从df中提取需要的数据;

plt.title('学生总成绩分布图')
plt.xlabel('学号')
plt.ylabel('总分')
plt.bar(name,students_scores)
#plt.figure()
plt.show()


#5.学生总成绩分布图;

plt.title('每门课程平均分展示图')
plt.xlabel('课程名')
plt.ylabel('平均分')
plt.bar('Python',Python_avg)
plt.bar('高数',math_avg)
plt.bar('英语',english_avg)
#plt.figure()
plt.show()

#6.每门课程平均分展示图;

plt.title('每门课程最高分展示图')
plt.xlabel('课程名')
plt.ylabel('最高分')
plt.bar('Python',Python_max)
plt.bar('高数',math_max)
plt.bar('英语',english_max)
#plt.figure()
plt.show()



#7.每门课程最高分展示图;


plt.title('每门课程最低分展示图')
plt.xlabel('课程名')
plt.ylabel('最低分')
plt.bar('Python',Python_min)
plt.bar('高数',math_min)
plt.bar('英语',english_min)
#plt.figure() #可以删除
plt.show()


#8.每门课程最低分展示图.
