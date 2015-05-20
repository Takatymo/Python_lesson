# -*- coding:utf-8 -*-

import sys
if __name__ == '__main__':
    with open('../address.txt', encoding='utf-8') as in_file,\
            open('outputfile.csv', 'w', encoding='utf-8') as out_file:
        input_number = int(sys.argv[1])
        for i, line in zip(range(input_number),in_file):#address.txtの行数がコマンドライン引数より小さければ全行出力
            out_file.write(line)