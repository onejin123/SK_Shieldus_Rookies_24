import pandas as pd
import numpy as np

# 0. 데이터 불러오기
df = pd.read_csv('train.csv')
#print(df.isnull().sum())

# 1. age 열 결측치 => 평균값 대체
df['Age'] = df['Age'].fillna(df['Age'].mean())
#print(df.isnull().sum())

# 2. Embarked 열 결측치 => 최빈값 대체
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
#print(df.isnull().sum())

# 3. Cabin 열 => 결측치 많으니 삭제
drop_cabin = df.dropna(axis=1)

# 4. 결측치 제거 확인
print(drop_cabin.isnull().sum())