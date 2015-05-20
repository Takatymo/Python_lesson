# -*- coding:utf-8 -*-

if __name__ == '__main__':
    with open('../col2.txt', encoding='utf-8') as in_file,\
            open('outputfile.txt', 'w', encoding='utf-8') as out_file:
        dict={}
        for line in in_file:
            line=line.rstrip()
            if line in dict:
                dict[line] += 1
            else:
                dict[line] =1

        for line in sorted(dict.items(), key=lambda x:x[1], reverse=True):
            out_file.write(line[0]+'\t'+str(line[1])+'\n')
