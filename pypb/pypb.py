from datetime import datetime
from logging import INFO, Formatter, StreamHandler, getLogger
from pathlib import Path


def build_logger():
    logger = getLogger(__name__)
    logger.setLevel(INFO)

    fmt = "[%(filename)s:%(lineno)d][%(levelname)s][%(asctime)s] %(message)s"
    stream_hander = StreamHandler()
    stream_hander.setFormatter(Formatter(fmt=fmt))
    logger.addHandler(stream_hander)
    return logger


logger = build_logger()


class PathBuilder:
    def __init__(self, init_dir: str = "."):
        self.path = Path(init_dir)

    def __str__(self):
        return self.path.__str__()

    def __repr__(self):
        return self.path.__repr__()

    def add_path(self, path: str) -> Path:
        self.path = self.path / path
        return self.path

    def add_date(self, date: datetime = datetime.today()) -> Path:
        ymd = date.strftime("%Y-%m-%d")
        self.path = self.path / ymd
        return self.path

    def add_params(self, params: dict) -> Path:
        str_params = "-".join(
            [f"{k}={v}" for k, v in params.items() if type(v) in [str, int, float]]
        )
        self.path = self.path / str_params
        return self.path

    def mkdir(self) -> Path:
        self.path.mkdir(parents=True, exist_ok=True)
        logger.info(f"Created: {self.path}")
        return self.path
