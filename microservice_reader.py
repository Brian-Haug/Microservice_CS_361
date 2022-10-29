import time


def read_function(pin):
    time.sleep(10)
    f = open(str(pin)+'.txt', 'r+')
    text = f.read()

    return text


file_info = read_function(4582)

print(file_info)