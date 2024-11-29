import sys
import csv
import select_subject
#import extract

try:   
    file = open('20231231.csv', 'r', encoding='CP949')

except:
    print("에러가 발생했습니다. 다시 시도해 주세요.")

else:
    selected_subject = select_subject.select(file)

    print("선택된 과목 : ", selected_subject)
    print("위 과목의 표준점수 분포 그래프는 다음과 같습니다.")
