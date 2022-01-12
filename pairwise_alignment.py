# pairwise alignment

def p_alain(s, t):

    # 二次元配列を用意
    # score_array = [[[スコア, (座標)]・・
    score_array = [[[0, (0, 0)] for x in range(len(t) + 1)] for y in range(len(s) + 1)]
    
    slists = list(" " + s)
    tlists = list(" " + t)

    for i in range(len(slists)):
        for j in range(len(tlists)):
            if i == 0 and j == 0:
                continue

            score = 1 if slists[i] == tlists[j] else -3  # 一致してるかスコアを出す
            S_top = [0, 0, 0]
            # 特定条件の場合にスコアを表に書き入れる
            if i - 1 < 0 or j - 1 < 0:
                S_top[0] = -float('inf')
            else:
                S_top[0] = (score_array[i - 1][j - 1][0] + score)

            if i - 1 < 0:
                S_top[1] = -float('inf')
            else:
                S_top[1] = (score_array[i - 1][j][0] - 5)

            if j - 1 < 0:
                S_top[2] = -float('inf')
            else:
                S_top[2] = (score_array[i][j - 1][0] - 5)

            score_array[i][j][0] = max(S_top)

            if S_top.index(max(S_top)) == 0:
                score_array[i][j][1] = (i - 1, j - 1)
                score_array[i][j].append("o")
            if S_top.index(max(S_top)) == 1:
                score_array[i][j][1] = (i - 1, j)
                score_array[i][j].append("u")
            if S_top.index(max(S_top)) == 2:
                score_array[i][j][1] = (i, j - 1)
                score_array[i][j].append("s")

    routs = []
    y = len(t)  # 最後のセル
    x = len(s)  # 最後のセル

    # 最後のセルから始まってｓcore_array[x][y][1]のタプルの座標をたどっている。
    while not (x == 0 and y == 0):  # 座標が（0.0）になるまでループ

        rout = score_array[x][y][1]
        muki = score_array[x][y][2]
        routs.append(muki)
        x = rout[0]
        y = rout[1]

    routs = list(reversed(routs))

    tlists = tlists[1:]
    slists = slists[1:]

    chain1 = []
    chain2 = []
    s_count = 0
    t_count = 0
    for i, r in enumerate(routs):
        if len(routs) > len(slists):
            slists.append("-")
        if len(routs) > len(tlists):
            tlists.append("-")

        if r == "o":
            chain1 += slists[i - s_count]
            chain2 += tlists[i - t_count]

        if r == "u":
            chain1 += slists[i - s_count]
            chain2 += "-"
            t_count += 1

        if r == "s":
            chain1 += "-"
            s_count += 1
            chain2 += tlists[i - t_count]

    amari = len(chain1) - len(chain2)

    if len(chain1) < len(chain2):
        for i in range(abs(amari)):
            chain1.append("-")
    if len(chain1) > len(chain2):
        for i in range(abs(amari)):
            chain2.append("-")

    print("".join(chain1))
    print("".join(chain2))


s_in = input("Enter Query Sequence :")
t_in = input("Enter Subject Sequence :")

p_alain(s_in, t_in)
