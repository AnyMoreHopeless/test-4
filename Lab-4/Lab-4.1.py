# TODO решите задачу

import json

def calculate_product_sum(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
        product_sum = sum(item['score'] * item['weight'] for item in data)
        rounded_sum = round(product_sum, 3)
        print( rounded_sum)
        return rounded_sum


json_filename = "input.json"
result = calculate_product_sum(json_filename)