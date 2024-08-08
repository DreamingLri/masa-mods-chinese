import json
import os
import shutil
import zipfile
import hjson

def hjson_to_json():
    hjson_list = [
        './masa-mods-chinese/litematica.hjson',
        './masa-mods-chinese/malilib.hjson',
        './masa-mods-chinese/minihud.hjson',
        './masa-mods-chinese/syncmatica.hjson',
        './masa-mods-chinese/tweakeroo.hjson',
        './masa-mods-chinese/itemscroller.hjson',
    ]

    output_json_list = [
        './assets/litematica/lang/zh_cn.json',
        './assets/malilib/lang/zh_cn.json',
        './assets/minihud/lang/zh_cn.json',
        './assets/syncmatica/lang/zh_cn.json',
        './assets/tweakeroo/lang/zh_cn.json',
        './assets/itemscroller/lang/zh_cn.json',
    ]

    for hjson_file, json_file in zip(hjson_list, output_json_list):
        hjson_data = hjson.load(open(hjson_file, 'r', encoding='utf-8'))

        # Convert the HJSON file to JSON
        
        output_dir = os.path.dirname(json_file)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        output_file = open(json_file, 'w', encoding='utf-8')
        output_file.write(json.dumps(hjson_data, ensure_ascii=False, indent=4))
        output_file.close()

def zip_files():
    def zip_files_and_folders(zip_filename, items_to_zip):
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for item in items_to_zip:
                if os.path.isdir(item):
                    for root, dirs, files in os.walk(item):
                        for file in files:
                            file_path = os.path.join(root, file)
                            arcname = os.path.relpath(file_path, os.path.dirname(item))
                            zipf.write(file_path, arcname)
                else:
                    zipf.write(item, os.path.basename(item))
    items_to_zip = [
        'assets',
        'pack.mcmeta',
        'pack.png',
    ]
    zip_filename = './masa-mods-chinese.zip'
    zip_files_and_folders(zip_filename, items_to_zip)

def delete_files():
    shutil.rmtree('./assets')

hjson_to_json()
zip_files()
delete_files()
print('Done!')
