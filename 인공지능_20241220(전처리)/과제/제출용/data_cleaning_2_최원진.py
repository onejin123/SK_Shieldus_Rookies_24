import pandas as pd

# 파일 불러온 후 중복된 데이터 개수 확인
df = pd.read_csv('sales.csv')
#print('중복된 데이터 개수 :', df.duplicated().sum())

# 중복된 데이터 삭제
no_dupl_df = df.drop_duplicates()
#no_dupl_df

# 데이터 개수 확인
print('남은 데이터 개수 : ', no_dupl_df.count().sum())
print('중복된 데이터 개수 :', no_dupl_df.duplicated().sum())