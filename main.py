# https://playground.learnqa.ru/api/map
# https://editor.swagger.io/
import json

from json.decoder import JSONDecodeError
import requests

import ast

# ------------------------------------------------------------------------------------------------------------

# ast.literal_eval("{'muffin' : 'lolz', 'foo' : 'kitty'}")
#
# payload = {'name': 'User'}
# response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
#
# response_dict = ast.literal_eval(response.text)
#
# print(response.text)
# print(response_dict["answer"])
# print(response_dict, type(response_dict))

# ------------------------------------------------------------------------------------------------------------


response = requests.get("https://playground.learnqa.ru/api/hello", params={'name': 'User'})
parsed_response_text = response.json()
print(parsed_response_text['answer'])

# ------------------------------------------------------------------------------------------------------------

response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)

try:
    parsed_response_text = response.json()
    print(parsed_response_text['answer'])
except JSONDecodeError:
    print('Response is not a JSON format')

# ------------------------------------------------------------------------------------------------------------