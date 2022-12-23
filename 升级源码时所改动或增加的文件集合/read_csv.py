from io import StringIO

import pandas as pd
import numpy as np

data = pd.read_csv('student_score.csv')

# print(data)
# print(type(data))
dd = data.to_dict()
# temp1 = dd['学号']
# print(temp1[0])
stuNn_Num = { }
for item_one in dd:
    # print(item_one, ":", dd[item_one])
    # temp = dd['学号']
    # print(dd[item_one]
    if item_one == '学号':
        stuNn_Num = dd[item_one]
    for item_two in dd[item_one]:
        str1 = stuNn_Num[item_two]
        str2 = item_one
        str3 = dd[item_one][item_two]
        print(str1)
        print(str2)
        print(str3)