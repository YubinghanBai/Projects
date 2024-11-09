import requests
from bs4 import BeautifulSoup

def get_synonyms(word):
    url = f"https://www.thesaurus.com/browse/{word}"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        synonyms = soup.find_all("a", {"class": "css-1hpgmv7 etbu2a32"})
        return [syn.text for syn in synonyms]
    else:
        print(f"Failed to fetch synonyms for {word}")
        return None

def save_synonyms_to_file(word, synonyms):
    with open("synonyms.txt", "a", encoding="utf-8") as file:
        file.write(word + ":\n")
        for syn in synonyms:
            file.write(syn + "\n")
        file.write("\n")

if __name__ == "__main__":
    while True:
        word = input("请输入要查询的单词（输入 'exit' 退出程序）：")
        if word.lower() == 'exit':
            break
        
        synonyms = get_synonyms(word)
        if synonyms:
            save_synonyms_to_file(word, synonyms)
            print(f"单词 '{word}' 的同义词已保存到 synonyms.txt 文件中。")
