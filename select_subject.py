import csv
import sys
import numpy as np

data = []

try:
    f = open('20231231.csv', 'r', encoding='CP949')
    columns = [0, 1]

    subjects = np.genfromtxt(f, delimiter=',', usecols=columns, skip_header=1, dtype=str, encoding='CP949')

    unique_subjects = np.unique(subjects, axis=0)
    #print(unique_subjects)

    order = ['국어', '수학', '사회탐구', '과학탐구', '직업탐구']

    order_dict = {key: i for i, key in enumerate(order)}
    sort_indices = np.argsort([order_dict[row[0]] for row in unique_subjects])

    sorted_subjects = unique_subjects[sort_indices]
    secondary_name_subject = np.empty(len(sorted_subjects), dtype=str)

    print(sorted_subjects)


    year = 2023

    print("이 수능 데이터는 %d 년의 데이터입니다. 연도를 선택하세요." %year)
    selected_year = input()

    


    i = 0
    for subject in sorted_subjects:
        print(subject[0], ":", subject[1])
        secondary_name_subject[i] = subject[1]
        i += 1

    print(secondary_name_subject)


    print("이 수능 데이터에 존재하는 과목은 위와 같습니다.\n조회를 원하시는 과목을 선택하세요.")
    selected_subject = input()
    while selected_subject not in secondary_name_subject:
        print("그런 과목 명은 없습니다. 다시 입력해 주세요.")
        selected_subject = input()


except csv.Error as e:
    print("Error")
    sys.exit(-1)
