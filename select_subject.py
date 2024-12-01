import csv
import numpy as np

#input  : file handle
#output : [과목 분류, 세부 과목명] 이 과목별로 저장되어 있는 2차원 ndarray
def find_subjects(file):
    data = []

    columns = [0, 1]

    subjects = np.genfromtxt(file, delimiter=',', usecols=columns, skip_header=1, dtype=str, encoding='CP949')

    unique_subjects = np.unique(subjects, axis=0)

    order = ['국어', '수학', '사회탐구', '과학탐구', '직업탐구']

    order_dict = {key: i for i, key in enumerate(order)}
    sort_indices = np.argsort([order_dict[row[0]] for row in unique_subjects])

    sorted_subjects = unique_subjects[sort_indices]

    return sorted_subjects

# input  : sjt_arr - [과목 분류, 세부 과목명] 이 과목별로 저장되어 있는 2차원 ndarray,
#          input_sjt : 사용자가 입력한 세부 과목명
#          selected_subjects : [선택된 과목의 분류, 선택된 세부 과목명] 형태의 1차원 배열
# output : 사용자가 입력한 세부 과목명의 존재 여부
def input_subject_check(sjt_arr, input_sjt, selected_subjects):

    extc = False

    if input_sjt in sjt_arr[:, 1]:
        extc = True 
        index = np.where(sjt_arr[:, 1] == input_sjt)[0][0]
        selected_subjects[0] = sjt_arr[index][0]
        selected_subjects[1] = sjt_arr[index][1]
    
    return extc


# input  : file handle
# output : [과목 분류, 세부 과목명] 이 과목별로 저장되어 있는 2차원 ndarray
def select(file):

    sjt_arr = find_subjects(file)

    year = 2024

    print("이 수능 데이터는 %d 년도 수능의 데이터입니다." %year)
    
    for subject in sjt_arr:
        print(subject[0], ":", subject[1])

    print("\n이 수능 데이터에 존재하는 과목은 위와 같습니다.\n조회를 원하시는 세부과목을 선택하세요.")
    input_subject = input()

    selected_subjects = [0, 0]
    while not input_subject_check(sjt_arr, input_subject, selected_subjects):
        print("그런 과목명은 없습니다. 다시 입력해 주세요.")
        input_subject = input()
        
    return selected_subjects

