import time
from model import IArray


def current_time_millis() -> int:
    return int(round(time.time() * 1000))


def test_add_array(data: IArray, total: int) -> None:
    start = current_time_millis()
    index = 0

    while index < total:
        data.add(time.time())
        index += 1

    end = current_time_millis()

    print("%s testAddArray: %sms." % (data, end - start))