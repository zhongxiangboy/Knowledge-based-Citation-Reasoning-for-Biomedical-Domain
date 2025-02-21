import jieba

text = "English is the English-language destination EXPRESSES_AeG for news and information about China. "
stext = " ".join(jieba.lcut(text))
print(stext)