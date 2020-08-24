import os

repo = '2013-shangdaxue/'
path = 'imgs/suijiang'
prefix = '![](https://cdn.jsdelivr.net/gh/xieqiaokang/' + repo
final_str = '<photos>'

img_list = os.listdir(path)

for img_name in img_list:
    img_str = prefix + path + '/' + img_name + ')'
    final_str += img_str

final_str += '</photos>'

print(final_str)