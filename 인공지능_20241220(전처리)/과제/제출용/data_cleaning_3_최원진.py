import pandas as pd

#1. 데이터 불러오기
df = pd.read_csv('diamonds.csv')
print('제거 전 데이터 개수 : ', df.count().sum())
#2. carat열 IQR 계산
Q1 = df['carat'].quantile(0.25)
Q3 = df['carat'].quantile(0.75)

IQR = Q3 - Q1

l_bound = Q1 - 1.5 * IQR
u_bound = Q3 + 1.5 * IQR

out_range = df[(df['carat']<l_bound) | (df['carat']>u_bound)]
print('이상치 개수 : ', out_range.count().sum())
#3. IQR 방식으로 이상치 제거 및 제거 후 데이터 개수 출력
df = df[(df['carat']>l_bound) & (df['carat']<u_bound)]
print('제거 후 데이터 개수 : ', df.count().sum())

#4. 상한값과 하한값 출력
print(f'상한 값 : {l_bound:2f}, 하한 값 : {u_bound}')