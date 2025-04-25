import os
from icrawler.builtin import GoogleImageCrawler

# 30 rastgele hayvan türü (çeşitli, karışık)
animals = [
    "cat", "dog", "elephant", "giraffe", "tiger", "lion", "zebra", "panda", "kangaroo", "koala",
    "rabbit", "horse", "cow", "sheep", "goat", "deer", "monkey", "bear", "fox", "wolf",
    "raccoon", "squirrel", "flamingo", "owl", "penguin", "eagle", "duck", "crocodile", "leopard", "hippopotamus"
]

# Ana klasör
root_dir = "data"

# Her hayvan için 50 görsel indir
for animal in animals:
    save_path = os.path.join(root_dir, animal)
    os.makedirs(save_path, exist_ok=True)

    print(f"[+] İndiriliyor: {animal}")
    crawler = GoogleImageCrawler(storage={'root_dir': save_path})
    crawler.crawl(keyword=f"{animal} animal", max_num=50)
    