#ダミー
# m_list_watched = [[1,1,0,0,1,0,1,0,1,1],
# [0,1,0,1,0,0,1,0,1,0],
# [1,0,1,1,0,1,0,0,1,0],
# [1,1,0,0,1,0,1,0,1,0],
# [0,0,1,0,0,1,0,0,1,1],
# [1,0,1,1,0,1,0,1,0,1],
# [0,1,0,0,1,0,1,0,1,0],
# [0,0,1,1,0,1,0,0,0,1]]

# url_list = ["aaa","bbb","ccc","ddd","eee","fff","ggg","hhh","iii","jjj"]

# url_list_user = ["aaa","ccc","ddd","fff","hhh","jjj","lll","mmm","vvv","rrr"]

import numpy as np

#ランキングを作るユーザーが見た動画をブール配列にする関数
def bool(url_list_user, url_list):
    l_bool = []

    for r in range(len(url_list)):
        if url_list[r] in url_list_user: #(シートの動画URLリスト)の中にユーザーが見た動画が入っていれば１
            l_bool.append(1)
        else: #入っていなかったら0
            l_bool.append(0)

    m_arr_user = np.array(l_bool)

    # print(m_arr_user)
    return(m_arr_user)

#コサイン類似度を求める関数
def cos_sml(l_1,l_2):
    if l_1 == 0:
           sml_cos = 0
    elif l_2 == 0:
          sml_cos = 0
    else:
           sml_cos= np.dot(l_1,l_2) / (np.linalg.norm(l_1) * np.linalg.norm(l_2))
    return sml_cos
#取ってきた各データに対するコサイン類似度を配列にする関数
def sml_l(m_arr_user,m_list_watched):
    sml = []

    for r in range(len(m_list_watched)):
        d = np.array(m_list_watched[r]) #最初のユーザーが見た動画リストを持ってくる
        sml.append(cos_sml(d,m_arr_user)) #調べたいユーザーとのコサイン類似度計算

    # print(sml)
    return(sml)

#ランキング作る関数
def rank(sml):
    sml_and_index = []

    for r in range(len(sml)):
        sml_and_index.append([r,sml[r]])

    arr_for_rank = np.array(sml_and_index)
    rank = arr_for_rank[np.argsort(arr_for_rank[:,1])[::-1]]
    rank_list = rank.tolist()

    for r in range(len(rank_list)):
        rank_list[r][0] = int(rank_list[r][0]) #float -> intに変換
        # rank_list[r][1] = (rank_list[r])[1]

    # print(rank_list)
    return(rank_list)

#合体させる
def matome(url_list, url_list_user, m_list_watched):
    m_arr_user = bool(url_list_user, url_list)
    sml = sml_l(m_arr_user, m_list_watched)

    place = 100 #ランキングの上位何位までを返すか
    ranking = rank(sml)[:place]

    return(ranking)


# print(matome(url_list_user,url_list,m_list_watched))
