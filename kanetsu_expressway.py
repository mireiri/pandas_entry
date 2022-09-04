# pandas
import pandas as pd

# グラフ作成で使うmatplotlib
import matplotlib.pyplot as plt

# matplotlibでも日本語を使えるようにするjapanize_matplotlib
import japanize_matplotlib


# サンプルデータの作成
'''
sample_df = pd.DataFrame(
  data,
  index,
  columns  
)
'''

# 2行5列のデータを用意
data = [[10, 20, 30, 40, 50], [100, 200, 300, 400, 500]]

# indexを用意
index = ['A', 'B']

# columns（列名）を用意
columns = ['one', 'two', 'three', 'four', 'five']

# データフレームを作成する
sample_df = pd.DataFrame(
    data=data,
    index=index,
    columns=columns
)

# データフレームを確認
print(sample_df)

# 列名を指定してデータを取得
print(sample_df['three'])

# 1行目1列目の"10"を取得する
print(sample_df.iloc[0, 0])

# 1列目から3列目までの列データを取得する
print(sample_df.iloc[:, :3])

# データを追加する
sample_df['six'] = [60, 600]
print(sample_df)

# データを編集
sample_df['six'] = sample_df['six'] / 10
print(sample_df)

# データを削除
sample_df = sample_df.drop('one', axis=1)
print(sample_df)

# 元のデータフレームを残したまま、新しいデータフレームを作成する
sample_df_rev = sample_df.drop('two', axis=1)
print(sample_df)
print(sample_df_rev)

sample2_df = pd.DataFrame(
    {'A': [1, 2, 3, 4, 5],
     'B': [10, 20, 30, 40, 50]   
     },
)
print(sample2_df)

# 折れ線グラフの作成
sample2_df.plot()

# matplotlibを使ったグラフ作成
fig, ax = plt.subplots()
ax.plot(sample2_df['A'], sample2_df['B'])
ax.grid()
plt.title('SAMPLE2')
plt.show()


# Excelファイルを読み込んでデータフレームで扱えるようにする
df = pd.read_excel('sapa_利用者数.xlsx')

# 結果を確認
print(df)

# 各列の最大値を確認
print(df.max())

# 各列の最小値を確認
print(df.min())

# 各列の平均値を確認
print(df.iloc[:, 1:].mean().round(1))

# 各列の中央値を確認
print(df.iloc[:, 1:].median().round(2))

# 各列の統計量を算出
print(df.describe())

# 日付列をindexに指定する
df = df.set_index('日付')
print(df)

print(df.index.weekday)

print(df.index.day_name())

# データフレームに曜日列を追加する
df['曜日'] = df.index.day_name()
print(df)

# 列名を取得する
print(df.columns)

# 列の並び替え
df = df.reindex(
    columns=[
        '曜日', '三芳', '高坂', '嵐山', '寄居', '上里',
        '駒寄', '赤城高原', '下牧', '谷川岳', 
        '土樽', '塩沢石打','大和', '堀之内', '越後川口', '山谷',
             ]
    )
print(df)

# 合計列を追加
df['合計'] = df.sum(axis=1)
print(df)

# 曜日でまとめたデータフレームを作成
Mon = df[df['曜日'] == 'Monday']
Tue = df[df['曜日'] == 'Tuesday']
Wed = df[df['曜日'] == 'Wednesday']
Thu = df.query('曜日 == "Thursday"')
Fri = df.query('曜日 == "Friday"')
Sat_Sun = df.query('曜日 == "Saturday" | 曜日 == "Sunday"')

print(Mon)
print(Tue)
print(Wed)
print(Thu)
print(Fri)
print(Sat_Sun)

# 折れ線グラフで可視化
fig, ax = plt.subplots()
x = Mon.iloc[:, 1: -1].columns
y = Mon.iloc[0, 1: -1]
ax.plot(x, y)
plt.xticks(rotation=90)
plt.title('第１週の月曜日')
plt.show()

# 複数の折れ線グラフ
fig, ax = plt.subplots()
x = Mon.iloc[:, 1: -1].columns
y1 = Mon.iloc[1, 1: -1]
y2 = Mon.iloc[2, 1: -1]
ax.plot(x, y1, color='blue', marker='*')
ax.plot(x, y2, color='green', marker='^')
plt.xticks(rotation=90)
plt.grid()
plt.title('第２週と第３週の月曜日')
plt.show()

# 一つの描画エリアに複数のグラフを配置
fig, ax = plt.subplots(ncols=2, figsize=(15, 5))

x_thu = Thu.iloc[:, 1: -1].columns
y_thu = Thu.iloc[1, 1: -1]

# 1つめのグラフ
ax[0].plot(x_thu, y_thu)
ax[0].set_title('木曜日')
ax[0].set_xticklabels(x_thu, rotation=90)
ax[0].set_ylim(0, 3500)
ax[0].grid()

x_fri = Fri.iloc[:, 1: -1].columns
y_fri = Fri.iloc[1, 1: -1]

# 2つめのグラフ
ax[1].plot(x_fri, y_fri)
ax[1].set_title('金曜日')
ax[1].set_xticklabels(x_fri, rotation=90)
ax[1].set_ylim(0, 3500)
ax[1].grid()

plt.subplots_adjust(wspace=0.2, hspace=0.6)
plt.show()


# 各SAPAの統計量を持ったデータフレームを作成
df_describe = df.describe()
print(df_describe)

# 合計列は不要なので削除
df_describe.drop(columns=['合計'], inplace=True)

# for文を使って各SAPAのmeanを取得
num = len(df_describe.columns)

for i in range(num):
    print(df_describe.iloc[1, i])

fig, ax = plt.subplots(figsize=(10, 8))
x_label = df_describe.columns
y_label = []

for i in range(num):
    y_label.append(df_describe.iloc[1, i])
    
ax.plot(
    x_label, y_label, marker='*', color='darkblue',
    linewidth=4, markersize=12
    )

plt.xticks(rotation=90)
plt.grid()
plt.title('SAPA-平均値')
plt.show()

# Excel形式にして出力する
df.to_excel('sapa.xlsx')

sample2_df.to_excel('sample.xlsx')

sample2_df.to_excel('sample.xlsx', index=False)

# おまけにもう一つのデータフレームもExcelに変換
df_describe.to_excel('sapa2.xlsx')


