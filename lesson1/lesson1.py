# -*- coding: utf-8 -*-

if __name__ == '__main__':
    with open('../address.txt', encoding='utf-8') as in_file:
        i = 0
        for line in in_file:
            i += 1

        print('The number of lows in the file \"',in_file.name,'\" is',i,'.')
