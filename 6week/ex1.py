import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import seaborn as sns

hat = pd.read_csv('ch4-2.csv') # hat 변수에 데이터셋 입력

font_path = "malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

# 히스토그램 그리기
plt.figure(figsize=(10, 17)) # 그래프 크기 지정
plt.hist(hat.weight, bins = 7)
plt.title('B 부화장 병아리 무게 분포 현황', fontsize = 17)
plt.xlabel('병아리 무게(g)')
plt.ylabel('마릿수')

# sns.displot(hat.weight)# 라인 히스토 그램으로 보기
plt.show()

# 상자그림 그리기
print(hat.describe(), end="\n\n")
plt.figure(figsize=(8, 10))
plt.boxplot(hat.weight)
plt.title('B hatchery chick weight box', fontsize=17)
plt.ylabel('weight(g)')
plt.show()


plt.subplot(1, 2, 1)
plt.hist(hat.weight)

plt.subplot(1, 2, 2)
plt.boxplot(hat.weight)

plt.show()