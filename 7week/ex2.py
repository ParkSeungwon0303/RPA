import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('2024_seoul_data.csv', encoding='utf-8')
df2 = df.fillna(method='ffill')
df2.info()

df2.rename(columns={'일강수량':'rain'}, inplace=True)

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False


plt.title('서울시 2024년도 여름 강수량 변화')
plt.plot(range(1, len(df2) + 1), df2['rain'], label='강수량', c='b')
plt.ylabel('강수량')
plt.legend()
plt.show()