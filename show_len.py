import json

file_zh = './assets/litematica/lang/zh.json'
file_en = './new_version/litematica/lang/en_us.json'
    
zh = json.load(open(file_zh, 'r', encoding='utf-8'))
en = json.load(open(file_en, 'r', encoding='utf-8'))

if len(zh) != len(en):
    print("The number of keys in the two files are different.")

for key in en:
    if key not in zh:
        print("\"{}\":\"{}\"".format(key, en[key]))