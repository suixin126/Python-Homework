import pandas as pd

# 1、数据读入与保存。将处理后的数据保存成excel（此步骤在后面的每一步中都要完成）。
# 读取csv文件
df = pd.read_csv('../source/movie_metadata.csv')

# 保存为Excel文件
df.to_excel('../source/movie_metadata.xlsx',index=False)

# 2、检查是否有缺失值和重复值，并进行处理。将处理后的数据展示5-10条。
# 处理方法：将包含缺失值的行删除
# df.dropna(inplace=True)
# 删除重复值
df.drop_duplicates(inplace=True)
# 如果数据少于10条，展示所有；否则展示前10条
# df1 = df.head(min(10, len(df)))
# 保存
# df1.to_excel('../source/data2-1.xlsx')

# 调试
# df.to_excel('../source/test.xlsx',index=False)

# 3、基于不同分组规则统计查看票房收入。
# 共3个子任务：
# 1）按照导演进行分组查看总票房，
grouped_by_director = df.groupby('director_name')['gross'].sum().reset_index()
# 保存
grouped_by_director.to_excel('../source/data3-1.xlsx',index=False)


# 2）按照男演员进行分组查看总票房
# 演员1
grouped_by_male_actor1 = df.groupby('actor_1_name')['gross'].sum().reset_index()
# 保存
grouped_by_male_actor1.to_excel('../source/data3-2-1.xlsx',index=False)

# 演员2
grouped_by_male_actor2 = df.groupby('actor_2_name')['gross'].sum().reset_index()
# 保存
grouped_by_male_actor2.to_excel('../source/data3-2-2.xlsx',index=False)

# 演员3
grouped_by_male_actor3 = df.groupby('actor_3_name')['gross'].sum().reset_index()
# 保存
grouped_by_male_actor3.to_excel('../source/data3-2-3.xlsx',index=False)


# 3）按照导演与演员的搭配分组并查看总票房。并分别保存为excel格式。
# 导演与演员1
df['director_actor1'] = df['director_name'].astype(str) + '_' + df['actor_1_name'].astype(str)
# # 按照导演与演员的搭配进行分组并计算总票房
grouped_by_director_actor1 = df.groupby('director_actor1')['gross'].sum().reset_index()
# # 保存为Excel文件
grouped_by_director_actor1.to_excel('../source/data3-3-1.xlsx', index=False)

# # 导演与演员2
df['director_actor2'] = df['director_name'].astype(str) + '_' + df['actor_2_name'].astype(str)
# # 按照导演与演员的搭配进行分组并计算总票房
grouped_by_director_actor2 = df.groupby('director_actor2')['gross'].sum().reset_index()
# # 保存为Excel文件
grouped_by_director_actor2.to_excel('../source/data3-3-2.xlsx', index=False)

# # 导演与演员3
df['director_actor3'] = df['director_name'].astype(str) + '_' + df['actor_3_name'].astype(str)
# # 按照导演与演员的搭配进行分组并计算总票房
grouped_by_director_actor3 = df.groupby('director_actor3')['gross'].sum().reset_index()
# # 保存为Excel文件
grouped_by_director_actor3.to_excel('../source/data3-3-3.xlsx', index=False)


# 4、科学计算。按照导演分组查看其最高票房的电影和最低票房的电影，并显示其余信息，包含上映时间等。将新数据保存为csv格式。
# 自定义函数:用于找到每个导演的最高和最低票房电影
def find_extremes(group):
    # 将确实数据处理为0
    group['gross'] = group['gross'].fillna(0)

    # 找到最高和最低票房电影的索引
    idx_max = group['gross'].idxmax()
    idx_min = group['gross'].idxmin()

    # 使用loc[]通过索引获取这些行
    max_movie = group.loc[idx_max]
    min_movie = group.loc[idx_min]

    # 将它们作为DataFrame返回，以便可以将它们合并在一起
    return pd.DataFrame({
        'color': [max_movie['color'], min_movie['color']],
        'director_name': [max_movie['director_name'], min_movie['director_name']],
        'num_critic_for_reviews': [max_movie['num_critic_for_reviews'], min_movie['num_critic_for_reviews']],
        'duration': [max_movie['duration'], min_movie['duration']],
        'director_facebook_likes': [max_movie['director_facebook_likes'], min_movie['director_facebook_likes']],
        'actor_3_facebook_likes': [max_movie['actor_3_facebook_likes'], min_movie['actor_3_facebook_likes']],
        'actor_2_name': [max_movie['actor_2_name'], min_movie['actor_2_name']],
        'actor_1_facebook_likes': [max_movie['actor_1_facebook_likes'], min_movie['actor_1_facebook_likes']],
        'gross': [max_movie['gross'], min_movie['gross']],
        'genres': [max_movie['genres'], min_movie['genres']],
        'actor_1_name': [max_movie['actor_1_name'], min_movie['actor_1_name']],
        'movie_title': [max_movie['movie_title'], min_movie['movie_title']],
        'num_voted_users': [max_movie['num_voted_users'], min_movie['num_voted_users']],
        'cast_total_facebook_likes': [max_movie['cast_total_facebook_likes'], min_movie['cast_total_facebook_likes']],
        'actor_3_name': [max_movie['actor_3_name'], min_movie['actor_3_name']],
        'facenumber_in_poster': [max_movie['facenumber_in_poster'], min_movie['facenumber_in_poster']],
        'plot_keywords': [max_movie['plot_keywords'], min_movie['plot_keywords']],
        'movie_imdb_link': [max_movie['movie_imdb_link'], min_movie['movie_imdb_link']],
        'num_user_for_reviews': [max_movie['num_user_for_reviews'], min_movie['num_user_for_reviews']],
        'language': [max_movie['language'], min_movie['language']],
        'country': [max_movie['country'], min_movie['country']],
        'content_rating': [max_movie['content_rating'], min_movie['content_rating']],
        'budget': [max_movie['budget'], min_movie['budget']],
        'title_year': [max_movie['title_year'], min_movie['title_year']],
        'actor_2_facebook_likes': [max_movie['actor_2_facebook_likes'], min_movie['actor_2_facebook_likes']],
        'imdb_score': [max_movie['imdb_score'], min_movie['imdb_score']],
        'aspect_ratio': [max_movie['aspect_ratio'], min_movie['aspect_ratio']],
        'movie_facebook_likes': [max_movie['movie_facebook_likes'], min_movie['movie_facebook_likes']],
        'extreme': ['max', 'min']
    })



# 应用自定义函数到按导演分组的DataFrame
extremes = df.groupby('director_name').apply(find_extremes).reset_index(drop=True)
# 将结果保存为CSV文件
extremes.to_csv('../source/data4-1.csv', index=False)
extremes.to_excel('../source/data4-1.xlsx', index=False)

# 5、基于电影类型的数据分析，查看不同类型电影的受欢迎。将数据保存为csv格式。
# 对电影类型进行分组，并计算每个类型的平均票房和平均评分
grouped_data = df.groupby('genres').agg({'gross':'mean','imdb_score':'mean'}).reset_index()
grouped_data.to_csv('../source/data5-1.csv',index=False)
grouped_data.to_excel('../source/data5-1.xlsx',index=False)
