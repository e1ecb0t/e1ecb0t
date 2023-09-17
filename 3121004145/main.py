import jieba
from gensim import corpora, similarities
import config
import re
import os

def get_txt(path):
    str = ''
    f = open(path, 'r', encoding='utf-8')
    line = f.readline()
    while line:  # 循环读文本
        str = str + line
        line = f.readline()
    return str


def filter(word):  # 将读取到的文件内容分词，过滤掉标点符号
    word = jieba.lcut(word)
    result = []
    for tags in word:
        if re.match(u"[a-zA-Z0-9\u4e00-\u9fa5]", tags):  # 正则表达式 匹配中文英文数字
            result.append(tags)
    return result


def cal_sim(txt1, txt2):
    content = [txt1, txt2]
    dict = corpora.Dictionary(content)
    corpus = [dict.doc2bow(txt) for txt in content]
    sim = similarities.Similarity('--Similarity-index', corpus, num_features=len(dict))
    temp_corpus = dict.doc2bow((txt1))
    cosine_sim = sim[temp_corpus][1]  # 余弦相似度
    return cosine_sim


if __name__ == '__main__':
    args = config.parse()
    path1 = args.read_path
    path2 = args.checking_path
    if not os.path.exists(path1):
        print('-----------------原文路径不存在--------------------')
        raise FileExistsError
    if not os.path.exists(path2):
        print('-----------------查重文件路径不存在------------------')
        raise FileExistsError
    result_path = args.result_path
    str1 = get_txt(path1)
    str2 = get_txt(path2)
    txt1 = filter(str1)
    txt2 = filter(str2)
    sim = cal_sim(txt1, txt2)
    print(f"相似度：{sim}")
    with open(result_path, 'a', encoding='utf-8') as f:
        f.write(f'{path1}与{path2}文章相似度:{sim}\n')
        f.close()
