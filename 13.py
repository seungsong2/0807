import numpy
import pandas as pd
import numpy as np

my_index = ['A', 'B', 'C']
my_columns =['이름', '나이', '성별']
my_data =numpy.array([
     ['Alice','Bob','홍길동'],
     [25, 30, 33],
     ['여','남','남']
])

df = pd.DataFrame(my_data, index= my_index, columns=my_columns)
print(df)

df.to_csv("./data.csv") #excel파일로 저장하는 코드