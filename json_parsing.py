import json

string_as_json_format = '{"answer": "Hello, User"}'
obj = json.loads(string_as_json_format)

# print(string_as_json_format)
# print(obj)
# print(obj['answer'])

key = 'answer'

if key in obj:
    print(f'Значение от ключа {key} - {obj[key]}')
else:
    print(f'Ключа {key} в JSON нет')
