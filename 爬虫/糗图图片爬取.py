import requests
import re
import os
###
if __name__=="__main__":
    if not os.path.exists('./qiutulibs'):
        os.mkdir('./qiutulibs')
    url='https://jandan.net/pic'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    page_text=requests.get(url=url,headers=headers).text
    ex = r'<div class="text">.*?<p>.*?<img src="(.*?)" style=.*?</p>'
    img_src_list = re.findall(ex,page_text,re.S)
    for src in img_src_list:
        ###拼接出一个完整的url
        src='https:'+src
        img_data=requests.get(url=src,headers=headers).content
        ###生成图片名称
        img_name=src.split('/')[-1]
        img_path='./qiutulibs/'+img_name
        with open(img_path,'wb') as fp:
            fp.write(img_data)
            print(img_name,'下载成功！')

