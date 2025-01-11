import pandas as pd
from sklearn.preprocessing import LabelEncoder

# 데이터 불러오기
df = pd.read_csv('adult.csv')

# 라벨 인코딩 열들 리스트에 넣고 인코딩
Encoding_list = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'gender', 'native-country']
label_encoder = LabelEncoder()
for encoded in Encoding_list:
    df[encoded] = label_encoder.fit_transform(df[encoded])