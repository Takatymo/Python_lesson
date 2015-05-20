# -*- coding:utf-8 -*-
if __name__ == '__main__':
    with open('../address.txt', encoding='utf-8') as in_file,\
            open('outputfile.txt', 'w', encoding='utf-8') as out_file:
        for line in in_file:
            out_file.write(line.replace('\t',' '))