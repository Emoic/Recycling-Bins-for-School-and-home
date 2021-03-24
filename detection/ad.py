# import csv
# def write_dict():
#     with open('phone.csv', 'w')as f:
#         writer = csv.DictWriter(f, fieldnames=('name', 'num'))
#         writer.writeheader()  # 写入头
#         writer.writerow({'name': 'swt', 'num': '1'})
#
#     print('写入成功')
#
# #write_dict()
# with open('phone.csv','a+')as f:
#     # reader = csv.DictReader(f,fieldnames=('name','num'))
#     # for i in reader:
#     #     print(i)
#     writer = csv.DictWriter(f, fieldnames=('name', 'num'))
#     writer.writerow({'name': 'pdy', 'num': '17'})
# # with open('phone.csv', 'w')as f:
#     writer = csv.DictWriter(f, fieldnames=('name', 'num'))
#     # writer.writeheader()  # 写入头
#     aa=reader
#     writer.writerow({'name': 'swt', 'num': '1'})

from collections import Counter
import cv2
a = ["ss", 4, "ss", 3, 2, 3, 4, 2]
c=["sts", 4, "sts", 3, "ss", 3, 4, 2]
b = Counter(a)  # 求数组中每个数字出现了几次
d=Counter(c)

print(d)
