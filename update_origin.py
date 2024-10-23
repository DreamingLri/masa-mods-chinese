import requests
import os

files = {
    'litematica': 'https://github.com/sakura-ryoko/litematica/raw/pre-rewrite/fabric/1.21.2/src/main/resources/assets/litematica/lang/en_us.json',
    'malilib': 'https://github.com/sakura-ryoko/malilib/raw/pre-rewrite/fabric/1.21.2/src/main/resources/assets/malilib/lang/en_us.json',
    'minihud': 'https://github.com/sakura-ryoko/minihud/raw/pre-rewrite/fabric/1.21.2/src/main/resources/assets/minihud/lang/en_us.json',
    'tweakeroo': 'https://github.com/sakura-ryoko/tweakeroo/raw/pre-rewrite/fabric/1.21.2/src/main/resources/assets/tweakeroo/lang/en_us.json',
    'itemscroller': 'https://github.com/sakura-ryoko/itemscroller/raw/pre-rewrite/fabric/1.21.2/src/main/resources/assets/itemscroller/lang/en_us.json',
    'syncmatica': 'https://github.com/sakura-ryoko/syncmatica/raw/1.21/src/main/resources/assets/syncmatica/lang/en_us.json',
    'litematica-printer': 'https://github.com/sakura-ryoko/litematica-printer/raw/1.21/src/main/resources/assets/litematica-printer/lang/en_us.json'
}

for name, url in files.items():
    r = requests.get(url)
    r.raise_for_status()
    path = os.path.join('masa-mods-chinese', 'en_us', name + '.json')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(r.content.decode('utf-8'))

print('Done!')
