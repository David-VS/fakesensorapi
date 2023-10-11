import dataclasses as dc
from datetime import datetime
import itertools


@dc.dataclass
class Measurement:
    id_iterator = itertools.count()

    m_id: int
    time: datetime
    temperature: float

    def __init__(self, temperature: float, time=datetime.now()) -> None:
        super().__init__()
        self.m_id = next(Measurement.id_iterator)
        self.temperature = temperature
        if isinstance(time, datetime):
            self.time = time
        else:
            raise ValueError(f"unsupported date format: {time}")







