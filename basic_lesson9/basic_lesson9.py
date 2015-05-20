# -*- coding:utf-8 -*-

if __name__ == '__main__':
    with open('../address.txt', encoding='utf-8') as in_file,\
            open('outputfile.txt', 'w', encoding='utf-8') as out_file:
        list=[]
        for line in in_file:
            list.append(line.split('\t',2))#住所の片方が登録されていない行があるので、要素数を２に指定

        sorted(list, key=lambda x:(x[1],x[0]), reverse=True)#要素数１の行がlistに入ればエラー

        for line in list:
            out_file.write('\t'.join(line))
