import MySQLdb
from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.pyplot as plt
from os import path
from PIL import Image 
import numpy as np

def _mod_word(content_list):
    content_text="".join(content_list)
    d=path.dirname(__file__)
    car_png=np.array(Image.open(path.join(d,"car.jpg")))
    wordclound=WordCloud(font_path='msyh.ttc',max_words=200000,mask=car_png).generate(content_text)
    image_colors=ImageColorGenerator(car_png)
    plt.imshow(wordclound.recolor(color_func=image_colors), interpolation="bilinear")
    plt.figure()
    plt.imshow(car_png,cmap=plt.cm.gray,interpolation='bilinear')
    plt.axis("off")
    plt.show()
    return 


db=MySQLdb.connect("localhost","root","","cms",charset="utf8")
cursor=db.cursor()
contexts=[]
sql="select title from cms_article"
try:
    cursor.execute(sql)
    results=cursor.fetchall()
    for row in results:
        context=row[0]
        contexts.append(context)
except:
    print "error"
db.close()
_mod_word(contexts)


