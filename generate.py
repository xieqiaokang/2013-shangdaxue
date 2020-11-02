import os

repo = '2013-shangdaxue'
path = 'imgs/shanghai'
prefix = '![](https://cdn.jsdelivr.net/gh/xieqiaokang/' + repo + '@master/'
final_str = '\n{% gallery %}\n'

img_list = os.listdir(path)

for img_name in img_list:
    img_str = prefix + path + '/' + img_name + ')\n'
    final_str += img_str

final_str += '{% endgallery %}\n'

print(final_str)