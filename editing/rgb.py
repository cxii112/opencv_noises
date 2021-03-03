def levels_rgb(cmp: float, pix):
    mod = (abs(cmp) % 1)
    if 0 <= mod < 1/3:
        return [0, 0, pix[2], 255]
    if 1/3 <= mod < 2/3:
        return [0, pix[1], 0, 255]
    if 2/3 <= mod <= 1:
        return [pix[0], 0, 0, 255]


def levels_ymc(cmp: float, pix):
    mod = (abs(cmp) % 1)
    if 0 <= mod < 1/3:
        return [0, pix[1], pix[2], 255]
    if 1/3 <= mod < 2/3:
        return [pix[0], 0, pix[2], 255]
    if 2/3 <= mod <= 1:
        return [pix[0], pix[1], 0, 255]


def levels_bmc(cmp: float, pix):
    mod = (abs(cmp) % 1)
    if 0 <= mod < 1/3:
        return [pix[0], 0, 0, 255]
    if 1/3 <= mod < 2/3:
        return [pix[0], 0, pix[2], 255]
    if 2/3 <= mod <= 1:
        return [pix[0], pix[1], 0, 255]
