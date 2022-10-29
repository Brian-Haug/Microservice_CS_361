
import time

time.sleep(5)

def text_doc_function(pin_number, data_dictionary):
    str_pin = str(pin_number)
    with open(str_pin+'.txt', 'w') as f:
        f.write(str(data_dictionary))

pin = 4582

workout_dict = {
    "day": "Tuesday",
    "group": "legs",
    "duration": "30"
}

text_doc_function(pin, workout_dict)