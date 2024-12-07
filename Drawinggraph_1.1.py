import numpy as np
import matplotlib.pyplot as plt

# 가공된 과목 안에서의 남자 배열, 여자 배열 순으로 매개인수 설정
# score_graph(남자 배열, 여자 배열)
def score_graph(arr_man, arr_woman, year):
    #제목 한글로 바꾸기
    plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.rcParams['axes.unicode_minus'] = False

    # 남자, 여자 별로 표준점수와 인원수 리스트 생성
    stand_score_man = [] # 남자 표준 점수
    pp_num_man = [] # 남자 인원수
    stand_score_woman = [] # 여자 표준 점수
    pp_num_woman = [] # 여자 인원수

    # arr_man이랑 arr_woman 배열 갯수가 같음
    # 배열 안에 있는 표준점수와 인원수 성별별로 분리해서 리스트에 append
    for i in range(len(arr_man)):
        stand_score_man.append(arr_man[i][2])
        pp_num_man.append(arr_man[i][3])

        stand_score_woman.append(arr_woman[i][2])
        pp_num_woman.append(arr_woman[i][3])

    # 분석 용이하게 하기 위해 numpy로 바꿈
    x1 = np.array(stand_score_man)
    y1 = np.array(pp_num_man)
    x2 = np.array(stand_score_woman)
    y2 = np.array(pp_num_woman)

    # 그래프 그리기
    plt.scatter(x1, y1, label = 'man')
    plt.scatter(x2, y2, label = 'woman')

    # 그래프 설정
    plt.legend(loc='best', ncol=2)
    plt.xlabel("표준점수")
    plt.ylabel("인원 수")
    # 제목에 입력받은 연도 및 과목 함께 표시
    plt.title(f"{year + 1}학년도 수능 {arr_man[0][1]} 과목 분포 ({year}년 실시)")

    # 그래프 표시
    plt.show()
