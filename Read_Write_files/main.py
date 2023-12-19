import os

open('3.txt', 'w').close()

with open('1.txt', 'r', encoding='utf-8') as file_1:
    sum_lines_1 = 0
    for line in file_1.readlines():
        sum_lines_1 += 1
#print(sum_line_1)

with open('2.txt', 'r', encoding='utf-8') as file_2:
    sum_lines_2 = 0
    for line in file_2.readlines():
        sum_lines_2 += 1
#print(sum_line_2)


with open('3.txt', 'a', encoding='utf-8') as file_3:
    with open('2.txt', 'r', encoding='utf-8') as file_2:
        with open('1.txt', 'r', encoding='utf-8') as file_1:
            if int(sum_lines_1) >= int(sum_lines_2):
                file_3.write(f'2.txt\n{sum_lines_2}\n')
                line = 0
                file_3.write(f'2.txt\n{sum_lines_2}\n\n')
                for line_ in file_2.readlines():
                    file_3.write(line_)
                file_3.write(f'\n\n1.txt\n{sum_lines_1}\n\n')
                for line_ in file_1.readlines():
                    file_3.write(line_)
            else:
                file_3.write(f'1.txt\n{sum_lines_1}\n\n')
                for line_ in file_1.readlines():
                    file_3.write(line_)
                file_3.write(f'\n\n2.txt\n{sum_lines_2}\n\n')
                for line_ in file_2.readlines():
                    file_3.write(line_)

with open('3.txt', 'r', encoding='utf-8') as file_3:
    print(file_3.read())
