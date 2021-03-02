import progressbar


def set_widgets(message: str, max_value: int, bounce: bool = False):
    bar = progressbar.Counter
    if bounce:
        bar = progressbar.BouncingBar
    widgets = [
        f'{message}...',
        ' (', bar(), f'/{max_value}) ',
        progressbar.Bar(left='[', right=']'),
        progressbar.ETA()
    ]
    return widgets
