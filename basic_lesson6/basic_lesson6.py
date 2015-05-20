# -*- coding:utf-8 -*-

import sys

if __name__ == '__main__':
    with open('../address.txt', encoding='utf-8') as in_file, open('outputfile.csv', 'w', encoding='utf-8') as out_file:

        """
        input_number：末尾から何行目か（コマンドラインから指定）
        p：p[i]はファイルの先頭からi行目の先頭までのバイト数
        """
        input_number = int(sys.argv[1])
        p=[]

        #p[i]を得るためのループ
        p.append(in_file.tell())
        line = in_file.readline()
        while line:
            p.append(in_file.tell())
            line = in_file.readline()

        #末尾からinput_number行目の先頭へシーク
        in_file.seek(p[len(p)-input_number-1])

        for line in in_file:
            out_file.write(line)