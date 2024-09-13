import json
import os
import shutil
import subprocess
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
        './masa-mods-chinese/litematica-printer.hjson',
    ]

    output_json_list = [
        './assets/litematica/lang/zh_cn.json',
        './assets/malilib/lang/zh_cn.json',
        './assets/minihud/lang/zh_cn.json',
        './assets/syncmatica/lang/zh_cn.json',
        './assets/tweakeroo/lang/zh_cn.json',
        './assets/itemscroller/lang/zh_cn.json',
        './assets/litematica-printer/lang/zh_cn.json',
    ]

    for hjson_file, json_file in zip(hjson_list, output_json_list):
        hjson_data = hjson.load(open(hjson_file, 'r', encoding='utf-8'))      
        output_dir = os.path.dirname(json_file)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        output_file = open(json_file, 'w', encoding='utf-8')
        output_file.write(json.dumps(hjson_data, ensure_ascii=False, indent=4))
        output_file.close()

def rename_mcmeta():
    def get_git_tags():
        try:
            result = subprocess.run(["git", "describe", "--tags", "--abbrev=0"], capture_output=True, text=True, check=True)
            tag = result.stdout.splitlines()
            return tag
        except subprocess.CalledProcessError as e:
            print(f"Error while running git command: {e}")
            return []

    tag = get_git_tags()

    with open('pack.mcmeta', 'r', encoding='utf-8-sig') as f:
        data = json.load(f)

    data['pack']['pack_format'] = 34
    data['pack']['description'] = '§e[1.21]MASA全家桶汉化包' + '-' + tag[0]

    with open('pack.mcmeta', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

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
rename_mcmeta()
zip_files()
delete_files()
print('Done!')
