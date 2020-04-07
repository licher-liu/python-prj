"""
pip install Pillow 安装pillow库
"""


from PIL import Image

img = Image.open("P02_Img2ASCii\\cat.JPG")

out = img.convert("L")  # 转换为灰度图片

# 获取图片大小尺寸
width, height = out.size


# 调整图片尺寸,注意图片的尺寸，不能太大，像素太多txt文件显示太宽
x_scale = 0.4
y_scale = x_scale * 0.5  # 输出到文本字符行高和字符宽度会有差别，需要调整变形
out = out.resize((int(width * x_scale), int(height * y_scale)))
out.show()  # 显示图片

width, height = out.size

# 创建需要构成图形的ACSII字符列表，按照灰度由黑到白排列(字符占的比例多少)
acsiis = "@%#*+=-. "
# 创建一个绘制图片的字符串
texts = ""
for row in range(height):
    for col in range(width):
        gray = out.getpixel((col, row))
        texts += acsiis[int(gray / 255 * (len(acsiis)-1))]
    texts += "\n"

with open("P02_Img2ASCii\\pic.txt", 'w') as f:
    f.write(texts)
list =['a','b', 'c']
