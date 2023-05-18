def solution(sticker):
    if (l := len(sticker)) <=3 : return max(sticker)
    elif l == 4 : return max(sticker[0]+sticker[2],sticker[1]+sticker[3])
    x1, y1, z1 = sticker[0], sticker[1], sticker[0]+sticker[2]
    x2, y2, z2 = 0, sticker[1], sticker[2]
    for i in sticker[3:]:
        x1, y1, z1 = y1, z1, max(x1, y1)+i
        x2, y2, z2 = y2, z2, max(x2, y2)+i
    return max(x1, y1, y2, z2)