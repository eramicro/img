import os

# 获取当前目录下所有后缀为png和jpg的图片路径
# 写入文本文档内

img_prefix = "https://jsd.proxy.aks.moe/gh/Zxis233/img2020S7@master/"
img_suffix = ['.png', '.jpg']
img_path = []
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if os.path.splitext(file)[1] in img_suffix:
            img_path.append(os.path.join(file))

with open('img.txt', 'w') as f:
    for path in img_path:
        f.write(img_prefix + path + '\n')
