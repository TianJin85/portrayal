from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import jieba


class maker_pl:

    def maker_png(mess_text, user_id):
        cut_text = jieba.cut(mess_text, cut_all=False)
        result = " ".join(cut_text)

        # 轮廓图片获取
        mask = np.array(Image.open(r'./static/bottom_model.png'))

        # #333943
        word_cloud = WordCloud(font_path='simhei.ttf', background_color=None, max_words=2000, repeat=True, mask=mask,min_font_size=1, mode='RGBA')
        # import ipdb;ipdb.set_trace()
        word_cloud.generate(result)

        backgroud_Image = plt.imread(r'./static/painting.jpg')
        mg_colors = ImageColorGenerator(backgroud_Image)
        word_cloud.recolor(color_func=mg_colors)
        word_cloud.to_file(r'./static/user_img/user_id{0}.png'.format(user_id))



