import progressbar


def set_widgets(message: str, max_value: int):
    widgets = [
        f'{message}...',
        ' (', progressbar.Counter(), f'/{max_value}) ',
        progressbar.Bar(left='[', right=']'),
        progressbar.ETA()
    ]
    return widgets
