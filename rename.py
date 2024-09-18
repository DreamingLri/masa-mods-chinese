import os
import shutil

if os.path.exists('./masa-mods-chinese.zip'):
    file_path = './masa-mods-chinese.zip'
    shutil.move(file_path, './[1.21]MASA全家桶汉化包.zip')

if os.path.exists('./masa-mods-chinese-new.zip'):
    file_path = './masa-mods-chinese-new.zip'
    shutil.move(file_path, './[1.21]MASA全家桶汉化包-new.zip')