# Microservice_CS_361

# The function text_doc_function(pin_number, data_dictionary) writes the provided dictionary to a text file named after the provided pin number.

# The function read_function(pin) reads the contents of text file with the name of the provided pin number.

# Both functions are in seperate .py files and not imported or linked in any way.

# ------------------------------------------------------------------------------------------------------------

# To REQUEST data: call function text_doc_function(pin_number, data_dictionary) in microservice_function.py

# Example:

# workout_dict =
# {
#    "day": "Tuesday",
#    "group": "legs",
#    "duration": "30"
# }
# pin = 88654

# text_doc_function(pin, workout_dict )

# ------------------------------------------------------------------------------------------------------------

# To RECEIVE data: call function read_function(pin) in microservice_reader.py

# Example:

# read_function(88654)

# Returns:
# {
#    "day": "Tuesday",
#    "group": "legs",
#    "duration": "30“
# }

![image](https://user-images.githubusercontent.com/81545762/198844196-9fa9ab00-ef78-4286-ad69-fa02fdec9044.png)

![image](https://user-images.githubusercontent.com/81545762/198844201-0a149cb7-77fb-4868-a7d9-a65be57f931d.png)

