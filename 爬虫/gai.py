import requests
import re
import os
import time

def sanitize_filename(filename):
    # 过滤非法字符
    return re.sub(r'[\\/*?:"<>|]', "", filename)

if __name__ == "__main__":
    # 创建文件夹
    if not os.path.exists('./qiutulibs'):
        os.mkdir('./qiutulibs')
    
    # 目标 URL 和请求头
    url = 'https://jandan.net/pic'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    
    try:
        page_text = requests.get(url=url, headers=headers).text
        print("Page content fetched successfully")
    except requests.RequestException as e:
        print(f"Error fetching the page: {e}")
        exit()
    
    # 打印部分网页内容进行调试
    print(page_text[:1000])  # 打印前1000个字符
    
    # 正则表达式提取图片 URL
    ex = r'<div class="text">.*?<p>.*?<img src="(//.*?\.(?:jpg|jpeg|png|gif))"'
    img_src_list = re.findall(ex, page_text, re.S)
    
    # 打印匹配到的图片 URL 列表进行调试
    print("Matched image URLs:")
    for src in img_src_list:
        print(src)
    
    if not img_src_list:
        print("No image URLs found. Exiting.")
        exit()
    
    for src in img_src_list:
        src = 'https:' + src  # 补全 URL
        print(f"Downloading {src}")
        
        try:
            response = requests.get(url=src, headers=headers)
            if response.status_code == 200:
                img_data = response.content
            else:
                print(f"Failed to download {src}: Status code {response.status_code}")
                continue
        except requests.RequestException as e:
            print(f"Error fetching the image {src}: {e}")
            continue
        
        img_name = src.split('/')[-1]
        img_name = sanitize_filename(img_name)  # 过滤非法字符
        img_path = './qiutulibs/' + img_name
        
        try:
            with open(img_path, 'wb') as fp:
                fp.write(img_data)
            # 打印图片文件路径和大小
            file_size = os.path.getsize(img_path)
            print(f"{img_name} 下载成功！文件大小：{file_size} 字节")
        except IOError as e:
            print(f"Error saving the image {img_name}: {e}")
        
        # 延时一段时间，以避免请求过于频繁
        time.sleep(1)
