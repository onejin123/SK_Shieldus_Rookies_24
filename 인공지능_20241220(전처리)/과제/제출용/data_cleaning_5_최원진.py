import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# 데이터 불러오기
Wine_df = pd.read_csv('winequality-red.csv')

#fixed acidity, volatile acidity, citric acid, residual sugar, chlorides 열의 값을 표준화
scaler_list = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides']
scaler_df = pd.DataFrame()
standard_scaler = StandardScaler()
for scaler in scaler_list:
    #표준화 후 데이터가 2차원 배열이라 구글링 후 뒤에 .flatten()으로 축소 후 1차원 배열로 만듬
    scaler_df[scaler] = standard_scaler.fit_transform(Wine_df[[scaler]]).flatten()

# 표준화한 열들의 데이터프레임 출력
print(scaler_df)