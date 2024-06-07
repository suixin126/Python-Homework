import pandas as pd
from numpy import NaN

data = {
    'grammer':["Python","C","Java","GO","R","SQL","PHP","Python"],
    'score':[1.0,2.0,NaN,4.0,5.0,6.0,7.0,10.0]
}

# 将字典转化为DataFrame
# df = pd.DataFrame.from_dict(data)
df = pd.DataFrame(data)
print(df)

# 提取含有字符串Python的行
filtered_df = df[df['grammer'].str.contains('Python', case=False)]
print(filtered_df)

# 输出df的所有列名
print(df.columns)

# 修改第二列列名为'popularity'
# df.columns.values[1] = 'popularity'
old_columns = df.columns.tolist()
old_columns[1] = 'popularity'
df.columns = old_columns
print(df)

# 统计grammer列中每种编程语言出现的次数
languageCounts = df['grammer'].value_counts()
print(languageCounts)

# 按照grammer列进行去重
dfUnique = df.drop_duplicates(subset='grammer',keep='first')
print(dfUnique)

# 修改popularity列，第三行的值
# df.at[2,'popularity'] = 2.0
# print(df)

# 计算popularity列平均值
averagePopularity = df.popularity.mean()
print(averagePopularity)

# 将grammer列转换为list
grammerList = df['grammer'].tolist()
print(grammerList)

# 将DataFrame保存为EXCEL
# df.to_excel('first.xlsx',index=False)  # index=False 表示不将DataFrame的行索引保存到Excel文件中。如果你希望保存索引，可以省略这个参数或将其设置为True

# 查看数据行列数
dfShape = df.shape
print(dfShape)

# 提取popularity列值大于3小于7的行
print(df[(df['popularity'] > 3) & (df['popularity'] < 7)])

# 交换两列位置
newOrder = ['popularity','grammer']
# df = df[newOrder]
# print(df)

# 提取popularity列最大值所在行
maxPopularityIndex = df['popularity'].idxmax()
result = df.iloc[[maxPopularityIndex]]
print(result)

# 查看最后5行数据
lastFiveRows = df.tail(5)
print(lastFiveRows)

# 添加一行数据['Perl',6.6]
newLine = {'grammer':'Perl','popularity':6.6}
newDf = df._append(newLine,ignore_index = True)
# df = newDf
# print(df)

# 对数据按照"popularity"列值的大小进行排序
sortedDf = df.sort_values(by='popularity')
print(sortedDf)

# pandas读取本地XCEL数据（文件名为pandas120）
# pandas读取本地CSV数据。
dfExcel = pd.read_excel('pandas120.xlsx')
print(dfExcel)

dfCsv = pd.read_csv('pandas120.csv')
print(dfCsv)

# 将下列数据根据学历进行分组并计算平均薪资
data1 = {
    'createTime':["2020-03-16 11:30:18",
                  "2020-03-16 10:58:48",
                  "2020-03-16 10:46:39",
                  "2020-03-16 10:45:44",
                  "2020-03-16 10:20:41"],
    'education':["本科","本科","不限","本科","本科"],
    'salary':[27500,30000,27500,16500,15000]
}

df1 = pd.DataFrame(data1)

averageSalaryByEducation = df1.groupby('education')['salary'].mean().reset_index()
print(averageSalaryByEducation)

# 将createTime列时间转换为月-日
# df1['createTime'] = pd.to_datetime(df1['createTime'])
# df1['month_day'] = df1['createTime'].dt.strftime("%m-%d")
# print(df1)

#  查看索引、数据类型和内存信息
print(df1.index)
print(df1.dtypes)
print(df1.info)

# 查看数值型列的汇总统计
numericCols = df1.select_dtypes(include=['int64','float64'])
print(numericCols.describe())

#  取出第3行数据
row33 = df1.iloc[2]
print(row33)

# 计算salary列的中位数
medianSalary = df1['salary'].median()
print(medianSalary)

# 将df的第一列与第二列合并为新的一列
df1['newCol1'] = df1['createTime'].astype(str) + df1['education'].astype(str)
print(df1)

# 将education列与salary列合并为新的一列
df1['newCol2'] = df1['education'].astype(str) + df1['salary'].astype(str)
print(df1)

#  将第2行数据添加至末尾
rowToAppend = df1.iloc[1]
df1Appended = df1._append(rowToAppend,ignore_index=True)
print(df1Appended)

# 将createTime列设置为索引
df1.set_index('createTime',inplace=True)
print(df1)

# 检查数据中是否含有任何缺失值
hasNullValues = df1.isnull().any().any()
print(hasNullValues)

#  将salary列类型转换为浮点数
df1['salary'] = df1['salary'].astype(float)
print(df1['salary'].dtype)

# 查看每种学历出现的次数
educationCounts = df1['education'].value_counts()
print(educationCounts)

# 删除所有存在缺失值的行
df1NoNull = df1.dropna()
print(df1NoNull)

# 导入并查看pandas版本
print(pd.__version__)

# 将df，df1，df2按照行合并为新DataFrame
df2 = pd.DataFrame(data)
dfCombined = pd.concat([df,df1,df2],ignore_index=True)
print(dfCombined)

# 修改列名为col1,col2,col3
columnMap = {'createTime':'col1','education':'col2','salary':'col3'}
#df1.rename(columns=columnMap,inplace=True)
print(df1)

# 按行计算df的每一行均值
data3 = {
    'A':[1,2,3],
    'B':[4,5,6],
    'C':[7,8,9]
}
df3 = pd.DataFrame(data3)
rowMeans = df3.mean(axis=1)
print(rowMeans)

# 将第一列大于50的数字修改为'高'
# df3['A'] = df3['A'].astype(str)
# df3.loc[df3['A'].astype(int) > 2,'A'] = '高'
# print(df3)

# 按照多列对数据进行合并df1和df2
mergedDf = pd.merge(df,df2,on=['grammer'],how='inner')
print(mergedDf)

#  对salary求平均，对popularity列求和
averageSalary = df1['salary'].mean()
totalScore = df['popularity'].fillna(0).sum()
print(averageSalary)
print(totalScore)

# 计算salary最大值与最小值之差
maxSalary = df1['salary'].max()
minSalary = df1['salary'].min()
salaryRange = maxSalary - minSalary
print(salaryRange)

# 将第一行与最后一行拼接
firstRow = df3.iloc[0]
lastRow = df3.iloc[-1]
combinedRow = pd.Series([firstRow['A'] + lastRow['A'],
                         firstRow['B'] + lastRow['B'],
                         firstRow['C'] + lastRow['C']
                         ],
                        index=df3.columns
                        )
df3 = df3._append(combinedRow,ignore_index=True)
print(df3)