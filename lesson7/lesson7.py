# -*- coding:utf-8 -*-

if __name__ == '__main__':
    with open('../address.txt', encoding='utf-8') as in_file:
        dict={}

        for line in in_file:
            list = line.split()
            if list[0] in dict:
                dict[list[0]] += 1
            else:
                dict[list[0]] =1

        print('address'+',\t'+'count number')
        for address, count_number in dict.items():
            print(address+',\t'+str(count_number))