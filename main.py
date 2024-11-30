import sys
import csv
import select_subject as ss
import extract
import Drawinggraph as dg

try:   
    file = open('20231231.csv', 'r', encoding='CP949')

except:
    print("에러가 발생했습니다. 다시 시도해 주세요.")

else:
    selected_subjects = ss.select(file)

    print("선택된 과목 : %s - %s" %(selected_subjects[0], selected_subjects[1]))
    print("위 과목의 표준점수 분포 그래프는 다음과 같습니다.")

    score_array = extract.get_arr('20231231.csv')

    wanted_sub_f = extract.get_subj_gen(score_array, selected_subjects[0], selected_subjects[1], 0)
    wanted_sub_m = extract.get_subj_gen(score_array, selected_subjects[0], selected_subjects[1], 1)

    dg.score_graph(wanted_sub_m, wanted_sub_f)

    
