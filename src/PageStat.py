import nltk
from nltk import pos_tag, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import re
import WikiRequests
#import matplotlib.pylab as pylab
# encoding=utf8
import sys

# Text cleansing and filtering adapted from this gist: https://gist.github.com/ameyavilankar/10347201

reload(sys)
sys.setdefaultencoding('utf8')

wr = WikiRequests.WikiRequests()
wr.queryPage("John Carmack")
page = wr.pages.next()["extract"].encode("utf-8").lower()

# We need a utf-8 encoded stop words list because otherwise they are 'not equal'
utf8StopWords = [word.encode("utf-8") for word in stopwords.words("english")]

tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(page)
filteredWords = filter(lambda token: token not in utf8StopWords, tokens)
text = ' '.join(filteredWords)
tagged = nltk.pos_tag(text)

#tagged = text.tagged_words(tagset='universal')

# This gives us the actual frequencies for the words in the corpus.
tag_fd = nltk.FreqDist(tag for (word, tag) in tagged)

# This gives us the words themselves. I like this one more :P
word_fd = nltk.FreqDist(word for (word, tag) in tagged)

print(word_fd.most_common())
