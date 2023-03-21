import time


def add_clock(func):
    def wrapper(*args, **kwargs):
        begin = round(time.time()*1000)
        result = func(*args, **kwargs)
        end = round(time.time()*1000)
        print(f"Время имполнения: {end - begin} мс")
        return result
    return wrapper
