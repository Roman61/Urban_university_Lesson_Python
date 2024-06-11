class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title: str = title
        self.duration: int = duration
        self.time_now: int = 0
        self.adult_mode: bool = adult_mode

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title












