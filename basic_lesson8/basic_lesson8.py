# -*- coding:utf-8 -*-

if __name__ == '__main__':
    with open('../address.txt', encoding='utf-8') as in_file,\
            open('outputfile.txt', 'w', encoding='utf-8') as out_file:
        list=[]
        for line in in_file:
            list.append(line.split())

        sorted(list, key=lambda x:x[0])

        for line in list:
            out_file.write('\t'.join(line))