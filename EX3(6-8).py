import re

def find_numbers(numbers_row):
    result_list = []
    for i in numbers_row:
        result_list.append(float(i))
    return result_list

def split_to_pairs(input_str):
    result = []
    numbers = re.findall(r'-?\d+(?:\.\d+)*', input_str)
    if numbers:
        for number in numbers:
            num_parts = number.split('.')
            for i in range(len(num_parts)-1):
                pair = f"{num_parts[i]}.{num_parts[i+1]}"
                result.append(pair)
    return result
def find_min_number(data):
    pattern = r'-?\d+(?:\.\d+)*'
    matches = re.findall(pattern, data)
    parsed_values = []
    for i in matches:
        parsed_values += split_to_pairs(i)

    float_numbers_row = find_numbers(parsed_values)
    if not float_numbers_row:
        return None
    else:
        return min(float_numbers_row)

def find_max_number(data):
    pattern = r'-?\d+(?:\.\d+)*'
    matches = re.findall(pattern, data)
    parsed_values = []
    for i in matches:
        parsed_values += split_to_pairs(i)

    float_numbers_row = find_numbers(parsed_values)
    if not float_numbers_row:
        return None
    else:
        return max(float_numbers_row)

def max_consecutive_digits(data):
    max_conc = 0
    cur_conc = 0
    for i in data:
        if i.isdigit():
            cur_conc += 1
        else:
            max_conc = max(max_conc, cur_conc)
            cur_conc = 0
    return max_conc


if __name__ == '__main__':

