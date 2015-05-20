# -*- coding:utf-8 -*-

if __name__ == '__main__':
    with open('../address.txt', encoding='utf-8') as in_file,\
            open('../col1.txt', 'w', encoding='utf-8') as out_file1, open('../col2.txt','w', encoding='utf-8') as out_file2:
        for line in in_file:
            list=line.split('\t')
            out_file1.write(list[0]+'\n')
            out_file2.write(list[1])