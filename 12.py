import pandas as pd

data = {
    '이름' : ['Alice','Bob','홍길동'],
    '나이' : [25, 30, 33],
    '성별' : ['여','남','남']
}

df = pd.DataFrame(data)
print(df)

df.to_csv("./data.csv") #excel파일로 저장하는 코드