import numpy as np

# 创建一个包含15个元素的NumPy数组，元素为随机生成的0到100之间的整数
random_array = np.random.randint(0, 101, 15)
print("原始数组:", random_array)

# 对数组进行升序排序
sorted_array_asc = np.sort(random_array)
print("升序排序后的数组:", sorted_array_asc)

# 展示排序前后的最小值变化（其实排序后最小值不变）
min_before = np.min(random_array)
min_after = np.min(sorted_array_asc)
print("排序前的最小值:", min_before)
print("排序后的最小值:", min_after)

# 对排序后的数组进行降序排序
sorted_array_desc = np.flipud(sorted_array_asc)
print("降序排序后的数组:", sorted_array_desc)

# 展示排序前后的最大值变化（其实排序后最大值不变）
max_before = np.max(random_array)
max_after = np.max(sorted_array_desc)
print("排序前的最大值:", max_before)
print("排序后的最大值:", max_after)