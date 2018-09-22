# !/usr/bin/env python3
# -*- coding: utf-8 -*-


"""The File Read Excel"""

__author__ = 'SunTree'


import pandas as pd
import os

# 读取excel文件内容
filePath = os.path.join('F:\Python\Android_multi_language', 'multi_language.xlsx')
df = pd.read_excel(filePath)
print(df)

# 查找对应文件，并追加内容
appendFile = os.path.join('F:\Python\Android_multi_language', 'res')

if not os.path.exists(appendFile):
    os.mkdir(appendFile)

# 语言对应的文件地址
resDict = {'英文': 'res_en.xml', '日语': 'res_ja.xml', '德语': 'res_ge.xml', '阿语': 'res_it,xml'}
# 遍历excel中的内容，根据国家在对应的文件中添加文案

for country in df.columns:
    if country == '文案':
        continue
    resPath = resDict[country]
    print('resPath', resPath, 'country', country)
    if resPath is None:
        continue
    resFile = os.path.join(r'F:\Python\Android_multi_language\res', resPath)
    # 读取excel中的内容
    for i in df.index:
        content = df.at[i, country]
        print('content', content.encode('utf-8'))
        with open(resFile, 'w') as f:
            f.write(r'<%s>%s<%s>' % (content, content, content))

