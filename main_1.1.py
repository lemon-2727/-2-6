import sys
import csv
import select_subject as ss
import extract
import Drawinggraph as dg

#시험 년도에 해당되는 파일 선택
year = ss.select_year()
file_name = str(year)+'1231.csv'
# 파일 열기 시도, 열리지 않는 등 에러 발생 시 execpt 로 이동
try:   
    file = open(file_name, 'r', encoding='CP949')

except:
    print("에러가 발생했습니다. 다시 시도해 주세요.")

# 문제 없이 파일을 읽을 수 있는 경우
else:
    
    selected_subjects = ss.select(file, year)

    print("선택된 과목 : %s - %s" %(selected_subjects[0], selected_subjects[1]))
    print("위 과목의 표준점수 분포 그래프는 다음과 같습니다.")

    score_array = extract.get_arr(file_name)

    wanted_sub_f = extract.get_subj_gen(score_array, selected_subjects[1], selected_subjects[0], '여성')
    wanted_sub_m = extract.get_subj_gen(score_array, selected_subjects[1], selected_subjects[0], '남성')

    dg.score_graph(wanted_sub_m, wanted_sub_f, year)

    exit()
