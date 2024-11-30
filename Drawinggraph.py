import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

def score_graph(arr_man, arr_woman):
    plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.rcParams['axes.unicode_minus'] = False

    stand_score_man = []
    pp_num_man = []
    stand_score_woman = []
    pp_num_woman = []

    # arr_man이랑 arr_woman 배열 갯수가 같음
    for i in range(len(arr_man)):
        stand_score_man.append(arr_man[i][2])
        pp_num_man.append(arr_man[i][3])

        stand_score_woman.append(arr_woman[i][2])
        pp_num_woman.append(arr_woman[i][3])

    x1 = np.array(stand_score_man)
    y1 = np.array(pp_num_man)
    x2 = np.array(stand_score_woman)
    y2 = np.array(pp_num_woman)

    plt.plot(x1, y1, label = 'man')
    plt.plot(x2, y2, label = 'woman')

    plt.legend(loc='best', ncol=2)
    plt.xlabel("표준점수")
    plt.ylabel("인원 수")
    plt.title(f"2024학년도 수능 {arr_man[0][1]} 과목 분포")

    plt.show()
