# !usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Android 多语言替换脚本
    通过读取Excel表格和匹配values/strings.xml中已添加的多语言，实现自动添加其他的语言
"""

import pandas as pd
import os
import re


# Step 1: 读取excel文件里的内容
file_path = os.path.join('/home/sunmeng/PythonSpace/excel_demo', 'live_multi_language.xlsx')
data = pd.read_excel(file_path)
# print(data)

# Step 2: 资源文件和语言的映射关系
# excel语言 columns 和资源文件对应关系
lang_dirt = {'阿语 Arabic': 'values-ar', '土语 Turkish': 'values-tr', '西语 Spanish': 'values-es',
             '印尼Indonesia': 'values-in', '德语 Germany': 'values-de', '法语 French': 'values-fr',
             '印地 Hindi': 'values-hi'}

# lang_dirt = {'阿语': 'values-ar', '土语': 'values-tr', '西语': 'values-es',
#              '印尼语': 'values-in', '德语': 'values-de', '法语': 'values-fr',
#              '印地语': 'values-hi'}

skip_values = ['<resources>', '</resources>']
key_columns = '英文 English'
# Android 项目位置
res_file = '/home/sunmeng/AndroidStudioProjects/CameraDemo/app/src/main/res/'


# 使用正则表达式获取对应的string名称和value
def get_str_value_name(line):
    # print(' Step 2 Get Format Value [', line, ']')
    f = r'^.*<string name="(.*)">(.*)</string>.*$'
    try:
        return re.match(f, line).groups()
    except Exception as e:
        return None


def append_value_to_file(values):
    # print(' Step 4 Append Value To File [', values[0], '-', values[1], ']')
    for k, v in lang_dirt.items():
        # 检测文件是否存在
        if not os.path.exists(os.path.join(res_file, v)):
            os.mkdir(os.path.join(res_file, v))
        # 创建strings.xml
        res_file_path = os.path.join(res_file, v + '/strings.xml')
        if not os.path.exists(res_file_path):
            with open(res_file_path, 'w') as res_f:
                res_f.write('<resources>\n\n</resources>\n')
        # 获取当前行对应国家的语言
        str_value = data.at[values[0], k]
        # 追加对应的文件
        # print(' Step 5 str_name[ ', values[1], '-', str_value, ']')
        with open(res_file_path, 'a') as f:
            f.write('    <string name="%s">%s</string>\n' % (values[1], str_value))


def check_value_in_excel_and_append(arr_str):
    print(' Step 3 Check Value In Excel [ ', arr_str[0], '-', arr_str[1], ']')
    for index, s_value in enumerate(data.get(key_columns)):
        if s_value.strip() == arr_str[1].strip():
            append_value_to_file([index, arr_str[0]])


# 读取values/strings.xml 内容，检测是否在excel文件内
with open(os.path.join(res_file, 'values/strings.xml'), 'r') as r:
    for line in r.readlines():
        print('Step 1 Get String value [', line, ']')
        s_line = line.strip()
        if s_line.endswith('\n'):
            s_line = s_line.replace('\n', '')
        if s_line in skip_values or s_line is '':
            continue
        else:
            result = get_str_value_name(s_line)
            if result is None:
                continue
            check_value_in_excel_and_append(result)



