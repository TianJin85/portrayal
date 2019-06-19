
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import jieba
#1 直接复制文本信息
#2 打开txt文本
with open (r'C:\Users\Administrator\Desktop\alice.txt', 'r') as fp:
   text=fp.read()
print(text)
cut_text = jieba.cut(text,cut_all=False)
result = " ".join(cut_text)
#轮廓图片获取
mask = np.array(Image.open(r'./static/model.jpg'))
# import ipdb;ipdb.set_trace()
# #333943
word_cloud=WordCloud(font_path='simhei.ttf', background_color=None, max_words=200, repeat=True, mask=mask, min_font_size=1, mode='RGBA')
word_cloud.generate(result)
backgroud_Image = plt.imread(r'./static/painting.jpg')
mg_colors = ImageColorGenerator(backgroud_Image)
word_cloud.recolor(color_func=mg_colors)
word_cloud.to_file(r'./static/mask_wordcloud1.png')

#显示效果图
plt.axis("off")
plt.imshow(word_cloud, interpolation="bilinear")
plt.show()