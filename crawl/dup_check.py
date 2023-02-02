"""
파일명 : dup_check.py
설 명 :
생성일 : 2023-02-01
생성자 : hamin
since 2023.01.09 Copyright (C) by Hamin All right reserved.
"""

import csv


def dup_check(csv_file_path):
    list = []
    count = 0
    with open(csv_file_path, 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if row not in list:
                list.append(row)
            else:
                count += 1
    print(count)

    with open(csv_file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(list)


def main():
    file_dir = "/Users/koodoyoon/Desktop/crawl_data/"
    file_list = ["connection.csv", "image.csv", "option_product.csv", "product.csv"]
    for file_name in file_list:
        file_path = file_dir+file_name
        dup_check(file_path)


main()
