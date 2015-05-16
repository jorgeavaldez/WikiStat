import nltk
from nltk import pos_tag, word_tokenize
import WikiRequests
import matplotlib.pylab as pylab
# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
wr = WikiRequests.WikiRequests()
wr.queryPage("John Carmack")
page = wr.pages.next()["extract"].encode("utf-8")

text = word_tokenize(page)
tagged = nltk.pos_tag(text)

#tagged = text.tagged_words(tagset='universal')
tag_fd = nltk.FreqDist(tag for (word, tag) in tagged)
word_fd = nltk.FreqDist(word for (word, tag) in tagged)

print(word_fd.most_common())
