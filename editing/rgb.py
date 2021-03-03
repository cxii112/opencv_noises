def levels(cmp: float, pix):
    mod = (abs(cmp) % 1)
    if 0 <= mod < 1/3:
        return [0, 0, pix[2], 255]
    if 1/3 <= mod < 2/3:
        return [0, pix[1], 0, 255]
    if 2/3 <= mod <= 1:
        return [pix[0], 0, 0, 255]
