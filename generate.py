import os

path = 'imgs/shanghai'
prefix = '![](https://cdn.jsdelivr.net/gh/xieqiaokang/mcc17_daily/'
final_str = '<photos>'

img_list = os.listdir(path)

for img_name in img_list:
    img_str = prefix + path + '/' + img_name + ')'
    final_str += img_str

final_str += '</photos>'

print(final_str)