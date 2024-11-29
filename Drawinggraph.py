import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

def score_graph(arr, input_subj):
    plt.rcParams['font.family'] = 'Malgun Gothic'
    plt.rcParams['axes.unicode_minus'] = False
    stand_score_man = []
    pp_num_man = []
    stand_score_woman = []
    pp_num_woman = []
    for i in range(len(arr)):
        if arr[i][1] == input_subj:
            if arr[i][4] == 1:
                stand_score_man.append(arr[i][2])
            else:
                stand_score_woman.append(arr[i][2])
    for i in range(len(arr)):
        if arr[i][1] == input_subj:
            if arr[i][4] == 1:
                pp_num_man.append(arr[i][3])
            else:
                pp_num_woman.append(arr[i][3])

    x1 = np.array(stand_score_man)
    y1 = np.array(pp_num_man)
    x2 = np.array(stand_score_woman)
    y2 = np.array(pp_num_woman)

    plt.plot(x1, y1, label = 'man')
    plt.plot(x2, y2, label = 'woman')
    plt.legend(loc='best', ncol=2)
    plt.title(f"2024학년도 수능 {input_subj} 과목 분포")
    plt.show()