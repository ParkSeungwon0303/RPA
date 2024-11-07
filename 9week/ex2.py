import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 상관 분석 : 두 변수간의 선형관계(직선으로 나타나는지) 
# 편차 평균 = 분산, 두 변수의 편차 곱 평균 = 공분산
# 공분산을 알면 방향(정방향/역방향), 강도(0 근접성)
# 공분산이 커도 상관성이 적은 경우가 있기 때문에 상관계수를 이용하는 것이 정확하다.
w = pd.read_csv('moving_keyword.csv')
print(w, end="\n\n")
print(w.head(10), end="\n\n")

w_n = w.iloc[:, 1:4]
print(w_n, end="\n\n")
w_cor = w_n.corr(method= 'pearson')
print(w_cor, end="\n\n")
plt.rc('font', family='Malgun Gothic')

sns.pairplot(w_n)


plt.figure(figsize= (10, 7))
sns.heatmap(w_cor, annot= True, cmap= 'Blues')
plt.show()