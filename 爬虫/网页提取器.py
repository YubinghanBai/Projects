import requests
from pyquery import PyQuery as pq
if __name__ == '__main__':
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'

    }
    url='https://www.google.com/search?q='

    question=input('What do you want to search in Google?')
    param={
        'query': question
    }

    results = requests.get(url=url,params=param,headers=headers)
    content=results.text
    file_name=question+ '.html'
    with open(file_name,'w',encoding='utf-8') as fp:
        fp.write(content)
    print(file_name,'保存成功！')
    