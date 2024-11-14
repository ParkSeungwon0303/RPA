import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

w = pd.read_csv('ch5-1.csv')
w_n = w.iloc[:, 1:5]

#상관분석 - 두 변수의 관계성을 확인하기 위해 / 두 변수의 관련성을 확인하는것 / 직선의 관계를 가지고 확인함
#회귀분석 - 두 변수의 인과관계를 알수 있다. 원인(독립변수)과 결과(종속변수)를 구분함 / 직선의 관계를 가지고 확인함

# smf.ols(formula='결과~원인', data=데이터프레임) 설정
model_lm = smf.ols(formula='weight ~ food', data = w_n)
# flt() 학습 실행
result_lm = model_lm.fit()
# 출력
result_lm.summary()

print(result_lm.summary())

plt.figure(figsize = (10,7))
plt.scatter(w.food, w.weight, alpha= .5)
plt.plot(w.food, w.food * 4.6684 + 78.1551, color = 'red')
plt.text(12.5, 130, 'weight = 4.6684 food + 78.1551', fontsize = 12)
plt.title('Scatter Plot')
plt.xlabel('fode')
plt.ylabel('weight')
plt.show()
