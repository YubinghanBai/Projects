import requests
import json

if __name__ == "__main__":
    # 初始化Colorama，兼容Windows命令提示符
    ### 请求的url
    url = "https://www.thesaurus.com/browse/"
    ### 进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    ### post请求的数据

    word = input("请输入要翻译的单词：")
    data = {
        'kw': word
    }
    ### 发送请求
    response = requests.post(url=url, data=data, headers=headers)

    ### 获取响应数据
    result = response.json()
    print(result)

    ### 保存数据
    with open("./word.json", "a", encoding="utf-8") as fp:
        for item in result['data']:
            fp.write(f"{item['k']}: {item['v']}\n")
        fp.write("\n")  # 添加空行以便区分不同的结果
    print("翻译完成！")
    print("翻译结果已保存到./word.json文件中")
    