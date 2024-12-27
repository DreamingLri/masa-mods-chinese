import re
import subprocess


def get_git_tags():
    try:
        result = subprocess.run(["git", "describe", "--tags", "--abbrev=0"], capture_output=True, text=True, check=True)
        tag = result.stdout.splitlines()
        return tag
    except subprocess.CalledProcessError as e:
        print(f"Error while running git command: {e}")
        return []

def auto_increment_version():
    tag = get_git_tags()[0]
    print(tag)
    match = re.match(r"^(v\d+)\.(\d+)\.(\d+)$", tag)
    if not match:
        raise ValueError(f"Invalid tag format: {tag}")
    major, minor, patch = match.groups()
    patch = int(patch) + 1
    return f"{major}.{minor}.{patch}"

tag = auto_increment_version()

changelog_file = './.github/changelog/' + tag + '-changelog.md'

template = f"""## {tag}
### 更新内容

#### itemscroller 
#### litematica-printer
#### litematica
#### malilib
#### minihud
#### syncmatica
#### tweakeroo

### 修复错误

#### itemscroller 
#### litematica-printer
#### litematica
#### malilib
#### minihud
#### syncmatica
#### tweakeroo

### 吐槽
"""

with open(changelog_file, 'w', encoding='utf-8') as f:
    f.write(template)

print('Done!')
