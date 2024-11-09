import requests
if __name__ == "__main__":
    url = "https://fanyi.baidu.com/mtpe-individual/multimodal"

    ### 进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    word = input("请输入要翻译的单词：")
    data = {
        'kw': word
    }
    response = requests.post(url=url, data=data, headers=headers)

    result = response.json()

    print(result)

# 保存翻译结果到 word.json
    with open("./word.json", "a", encoding="utf-8") as fp:
        for item in result['data']:
            fp.write(f"{item['k']}: {item['v']}\n")
        fp.write("\n")  # 添加空行以便区分不同的结果
    print("翻译完成！")
    print("翻译结果已保存到./word.json文件中")
    # 若需要获取同义词，请在此处添加代码
    # synonyms = result['synonyms']
    # print("同义词：", synonyms)
    # 若需要获取音标，请在此处添加代码
    # phonetic = result['phonetic']
    # print("音标：", phonetic)
    # 若需要获取例句，请在此处添加代码
    # sentence = result['sentence']
    # print("例句：", sentence)
    # 若需要获取翻译的拼音，请在此处添加代码
    # pinyin = result['pinyin']
    # print("拼音：", pinyin)
    # 若需要获取翻译的发音，请在此处添加代码
    # pronunciation = result['pronunciation']
    # print("发音：", pronunciation)
    # 若需要获取翻译的字义，请在此处添加代码
    # translation = result['translation']
    # print("字义：", translation)
    # 若需要获取翻译的生词，请在此处添加代码
    # word_meaning = result['word_meaning']
    # print("生词：", word_meaning)
    # 若需要获取翻译的词性，请在此处添加代码
    # word_property = result['word_property']
    #
    # print("词性：", word_property)