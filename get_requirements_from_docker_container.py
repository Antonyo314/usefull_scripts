# docker exec 8af742b822df pip list > requirments_.txt

text = open('/home/anton/PycharmProjects/latentai-application-framework/requirements_.txt', 'r').read()

text = text.split('\n')
text = text[2:]

text = ['=='.join(i.split()) for i in text]
text = '\n'.join(text)

open('/home/anton/PycharmProjects/latentai-application-framework/requirements.txt', 'w').write(text)
