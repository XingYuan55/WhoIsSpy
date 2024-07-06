import random
import os


__default_words = [  # 原始词数据
        "摩托车——电动车",
        "汉堡包——肉夹馍",
        "高跟鞋——增高鞋",
        "水盆——水桶",
        "牛奶——豆浆",
        "海豚——海狮",
        "唇膏——口红",
        "烤肉——涮肉",
        "小矮人——葫芦娃",
        "作文——论文",
        "油条——麻花",
        "眉毛——胡须",
        "酸菜鱼——水煮鱼",
        "包青天——狄仁杰",
        "面包——蛋糕",
        "鸭舌帽——遮阳帽",
        "摩托车——电动车",
        "壁纸——贴画",
        "壁纸——贴画",
        "哈密瓜——西瓜",
        "海豚——海狮",
        "勇往直前——全力以赴",
    ]

def distribute_words(words: list = __default_words, nop=3):
    num = nop  # 人数
    treatmented_words = []  # 可识别词
    for i in words:
        treatmented_words += (i.split("——"),)

        
    # 选择词
    wordgroup = random.choice(treatmented_words)


    spy_word = random.choice(wordgroup)  # 卧底词
    normals_word = wordgroup[1-wordgroup.index(spy_word)]  # 平民词

    # 选择卧底
    spy_number = random.randint(1, num)
        
    res_words = []
    for player in range(1, num+1):
        # input()
        # os.system("cls")
        if player == spy_number:
            res_words += (spy_word,)
        else:
            res_words += (normals_word,)
            
    return (res_words, spy_word, normals_word)


if __name__ == "__main__":
    print(distribute_words())
