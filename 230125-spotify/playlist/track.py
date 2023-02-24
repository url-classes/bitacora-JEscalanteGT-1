class Track:
    def __init__(
        self,
        name: str,
        duration: int,
        album_cover: str,
        artists: list[str]
    ):
        self.name = name
        self.duration = duration
        self.album_cover = album_cover
        self.artists = artists
