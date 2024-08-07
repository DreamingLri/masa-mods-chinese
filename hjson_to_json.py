import json
import hjson

# Load the HJSON file
hjson_list = [
    './contributing/assets/litematica/lang/zh_cn.hjson',
    './contributing/assets/malilib/lang/zh_cn.hjson',
    './contributing/assets/minihud/lang/zh_cn.hjson',
    './contributing/assets/syncmatica/lang/zh_cn.hjson',
    './contributing/assets/tweakeroo/lang/zh_cn.hjson',
    './contributing/assets/itemscroller/lang/zh_cn.hjson',
]

morden_json_list = [
    './modern/assets/litematica/lang/zh_cn.json',
    './modern/assets/malilib/lang/zh_cn.json',
    './modern/assets/minihud/lang/zh_cn.json',
    './modern/assets/syncmatica/lang/zh_cn.json',
    './modern/assets/tweakeroo/lang/zh_cn.json',
    './modern/assets/itemscroller/lang/zh_cn.json',
]

classic_json_list = [
    './classic/assets/litematica/lang/zh_cn.json',
    './classic/assets/malilib/lang/zh_cn.json',
    './classic/assets/minihud/lang/zh_cn.json',
    './classic/assets/syncmatica/lang/zh_cn.json',
    './classic/assets/tweakeroo/lang/zh_cn.json',
    './classic/assets/itemscroller/lang/zh_cn.json',
]

for hjson_file, json_file in zip(hjson_list, classic_json_list):
    hjson_data = hjson.load(open(hjson_file, 'r', encoding='utf-8'))

    # Convert the HJSON file to JSON
    json_file = open(json_file, 'w', encoding='utf-8')
    json_file.write(json.dumps(hjson_data, ensure_ascii=False))
    json_file.close()