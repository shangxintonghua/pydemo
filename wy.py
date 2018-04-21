import requests;
import json;
from pyecharts import Bar
from wordcloud import WordCloud
import matplotlib.pyplot as plt

url="http://music.163.com/weapi/v1/resource/comments/R_SO_4_551816010?csrf_token="
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
    'Referer':'http://music.163.com/song?id=551816010',
    'Origin':'http://music.163.com',
    'Host':'music.163.com'
}
user_data={
    "params":"sKzgcamBruerTM/Cq1sTHOui5KpFiHIAf4Y8GK9hWUHQY9os/oEqFgT/Am7V0mMl8qpCBccnUH6s1FjS88/eloUu5SNiHZvFEMdrUoByj1+XVhckOn4PEFmuwlBh4C5zbTHaZxJFtUcST/+3/+x6XLkigWSiC31goKwEQXVcf1k3qXfCdjJjbc9ZfxWCjJRh",
    "encSecKey":"036a689a2a91cc5302b9d81a82c77cfc4d6ccfe5674e08cf93caadeac848f5f39480bf9aba166f607608bf12a881518703a3337818c12b8226eea7dd6a0f704a5c43ba300c29dd9b663f3679412a175c36ad9c9b7ef4a7958e47dab784ddcf96a22ec06bea1e63abfdeaf27581d1d304093fc7b336d71d9ad9547d7129a78300"
}
response=requests.post(url,headers=headers,data=user_data)
data=json.loads(response.text)
hotcomments=[]
for hotcomment in data['hotComments']:
    item={
        'nickname':hotcomment['user']['nickname'],
        'content':hotcomment['content'],
        'likedCount':hotcomment['likedCount']
    }
    hotcomments.append(item)
content_list=[content['content'] for content in hotcomments]
nickname=[content['nickname'] for content in hotcomments ]
liked_count=[content['likedCount'] for content in hotcomments]

bar=Bar("hot comment like count")
bar.add("like comment count",nickname,liked_count,is_stack=True,mark_line=["min","max"],mark_point=["average"])
bar.render()


content_text="".join(content_list)
wordclound=WordCloud(font_path='msyh.ttc',max_words=200).generate(content_text)
plt.figure()
plt.imshow(wordclound,interpolation='bilinear')
plt.axis("off")
plt.show()