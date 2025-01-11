import joblib
from sklearn.datasets import make_regression

X, y = make_regression(n_samples=100, n_features=1, noise=0.1)

# 모델 로드
loaded_model = joblib.load('linear_model.pkl')
print("Model loaded successfully.")
 # 모델 사용
y_pred = loaded_model.predict(X)
print(y_pred)

'''
객체를 파일로 저장하는 것을 직렬화라고한다.
파일을 객체로 하는 것을 역직렬화라고 한다.


데이터셋 가져오는곳
aihub(이상행동 감지 데이터셋, [보안]), kaggle, huggingface
https://www.kaggle.com/datasets/meetnagadia/human-action-recognition-har-dataset => 사람의 동작을 판단하는 모델 학습해보던가...?

https://paperswithcode.com/datasets?ref=blog-ko.superb-ai.com

'''