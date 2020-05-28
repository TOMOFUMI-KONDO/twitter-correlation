import numpy as np
#ダミー
m_list_watched = [[1,1,0,0,1,0,1,0,1,1],
[0,1,0,1,0,0,1,0,1,0],
[1,0,1,1,0,1,0,0,1,0],
[1,1,0,0,1,0,1,0,1,0],
[0,0,1,0,0,1,0,0,1,1],
[1,0,1,1,0,1,0,1,0,1],
[0,1,0,0,1,0,1,0,1,0],
[0,0,1,1,0,1,0,0,0,1]]

url_list = ["aaa","bbb","ccc","ddd","eee","fff","ggg","hhh","iii","jjj"]

url_list_user = ["aaa","ccc","ddd","fff","hhh","jjj","lll","mmm","vvv","rrr"]

#検索したいユーザーが見た動画をブール化する関数を作る
def bool(l_1,l_2):
    l_bool= []
    r=0
    for r in range(len(l_2)):
    #動画のURLリストの中にユーザーが見た動画が入っていれば１
        if l_1[r] in l_2:
            l_bool.append(1)
    #そうじゃなかったら０
        else:
            l_bool.append(0)
    m_arr_user=np.array(l_bool)
    print(m_arr_user)
    return(m_arr_user)

#コサイン類似度を求める関数を作る
def cos_sml(l_1,l_2):
    return np.dot(l_1,l_2) / (np.linalg.norm(l_1) * np.linalg.norm(l_2))

#取ってきた各データに対するコサイン類似度を配列にする関数を定義
def sml_l(l_1,l_2):
    sml = []
    r=0
    for r in range(len(l_2)):
    #最初のユーザーが見た動画リストを持ってくる
        d = np.array(l_2[r])
    #調べたいユーザーとのコサイン類似度計算
        sml.append(cos_sml(d,l_1))
    print(sml)
    return(sml)
#ランキング作る関数
def lank(sml):
    sml_and_index = []
    r=0
    for r in range(len(sml)):
        each_sml =[r,sml[r]]
        sml_and_index.append(each_sml)
    arr_for_lank=np.array(sml_and_index)
    lank=arr_for_lank[np.argsort(arr_for_lank[:,1])[::-1]]
    lank_list=lank.tolist()
    for r in range(len(lank_list)):
        (lank_list[r])[0]=int((lank_list[r])[0])
        (lank_list[r])[1]=(lank_list[r])[1]
    print(lank_list)
    return(lank_list)

#合体させる
def matome(url_list,url_list_user,m_list_watched):
     m_arr_user = bool(url_list_user,url_list)
     sml=sml_l(m_arr_user,m_list_watched)
     return(lank(sml)[0:5])


print(matome(url_list_user,url_list,m_list_watched))
