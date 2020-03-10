import re
import os
import sys
from fnmatch import fnmatch


def get_titles(path):
    # 打开文件获取标题，返回列表
    titles = []
    with open(path, 'r', encoding='utf - 8') as f:
        titles = re.findall(r'\n###\s(.*)\n', f.read())

    for i in titles:
        i.strip()
    return titles


def Write_catelog(file_names, titles):
    global base_path
    catelog_name = base_path+'README.md'
    date = []
    for i in range(len(file_names)):
        date.append(re.findall(r'note(\d+.\d+.\d+).md', file_names[i])[0])

    with open(catelog_name, 'w', encoding='utf-8') as f:
        f.write('# 目录\n')
        for i in range(len(titles)):
            f.write(f'## [{date[i]}](./Note/{file_names[i]})\n')
            f.write('### 内容：\n')
            for title in titles[i]:
                f.write(f'* {title}\n')


base_path = 'F:\\kiven\\Note\\'
chose_modle = '''模式:
1.生成目录
2.查看单个文件的标题
3.退出\n
输入你的选项（序号）：'''

while True:
    flag = input(chose_modle)
    # 获取执行模式
    if flag == '1':
        # 生成目录
        temp = os.listdir(base_path)
        file_names = []

        for name in temp:
            if fnmatch(name, 'note*.md'):
                file_names.append(name)

        titles = []
        for file_name in file_names:
            path = base_path+file_name

            titles.append(get_titles(path))

        Write_catelog(file_names, titles)
        print('\n完成！\n')

    elif flag == '2':
        # 获取标题
        file_name = input('\n请输出你要查看的文件名：')
        path = base_path+file_name

        if os.path.isfile(path):  # 若文件存在
            titles = get_titles(path)
            print('\n\n', '-'*20)
            for i in titles:
                print('* '+i)
            print('-'*20, '\n\n')

        else:
            print('文件不存在！')

    elif flag == '3':
        print('感谢使用！')
        break

    else:
        print('无效的序号！')
