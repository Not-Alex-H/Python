#basketball efficiency calculator
import os
def effic(pts, ast, reb, blk, stl, trn, fgm, fga):
    points = pts / 10 + ast / 3 + reb / 5 + blk + stl + trn * -2 + fga - fgm * -0.1
    return points
def test(r, a):
    if r == a:
        print("success")
    else:
        print("fail")
os.system('cls')
print("Hakeem Olajuwon quadruple double: " + str(effic(29, 9, 18, 11, 5, 0, 13, 25)))
print("Wilt Chamberlain quintuple double: " + str(effic(53, 14, 32, 24, 11, 1, 23, 30)))