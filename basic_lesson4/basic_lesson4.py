# -*- coding:utf-8 -*-

if __name__ == '__main__':
    with open('../col1.txt', encoding='utf-8') as in_file1, open('../col2.txt', encoding='utf-8') as in_file2,\
            open('../col1_to_2.txt', 'w', encoding='utf-8') as out_file:
        line1 = in_file1.readline()
        line2 = in_file2.readline()
        while line1 and line2:
            out_file.write(line1.rstrip('\n') + '\t' + line2)
            line1 = in_file1.readline()
            line2 = in_file2.readline()