
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import jieba
#1 直接复制文本信息
#2 打开txt文本
with open (r'C:\Users\Administrator\Desktop\会员画像.txt', 'r') as fp:
   text=fp.read()
print(text)
cut_text = jieba.cut(text,cut_all=False)
result = " ".join(cut_text)
#轮廓图片获取
mask=np.array(Image.open('erci.png'))
# import ipdb;ipdb.set_trace()
word_cloud=WordCloud(font_path='simhei.ttf', background_color='#333943', max_words=2000,repeat=True, mask=mask,min_font_size=1)
word_cloud.generate(result)
backgroud_Image = plt.imread('未标题-1.jpg')
mg_colors = ImageColorGenerator(backgroud_Image)
word_cloud.recolor(color_func=mg_colors)
word_cloud.to_file('mask_wordcloud1.png')

#显示效果图
plt.axis("off")
plt.imshow(word_cloud, interpolation="bilinear")
plt.show()