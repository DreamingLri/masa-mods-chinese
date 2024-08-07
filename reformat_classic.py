import json

litematica_zh = json.load(open('./assets/litematica/lang/zh_cn.json', 'r', encoding='utf-8')) 
litematica_en = json.load(open('./new_version/litematica/lang/en_us.json', 'r', encoding='utf-8')) 

data = {}

for key_en in litematica_en:
    for key_zh in litematica_zh:
        if key_zh == key_en.split('.')[-1]:
            if key_en.split('.')[-2] == 'name':
                data[key_en] = litematica_zh[key_zh]
        elif (key_zh == litematica_en[key_en]) & (key_en.split('.')[-2] == 'comment'):
            data[key_en] = litematica_zh[key_zh]
        

new = open('./assets/litematica/lang/zh.json', 'w', encoding='utf-8')
new.write(json.dumps(data, ensure_ascii=False))

