import json

# 字符串转为字典
text = '{"kang":12}'
print(text)
dit = json.loads(text)
print(type(dit))

# json.dumps 用于将 Python 对象编码成 JSON 字符串。
data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
js = json.dumps(data)
print(js)
