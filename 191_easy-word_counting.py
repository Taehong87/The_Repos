import urllib2, re
book = urllib2.urlopen('http://www.gutenberg.org/cache/epub/47498/pg47498.txt').read()
#book = """ hello. This is a story about my re-entry into the immigration system.
#            It starts with my collection of coffee mugs. I always felt that more than anything,
#            I needed to do something to help those poor people trying to enter the country.
#            However, there was an issue. I didn't know what I could do to make sure that they
#            wouldn't be abused once they entered the country. How could I possibly do this?
#            I can't exactly tell you. But I can tell you, I did the best that I could.
#        """

words = re.split('\W', book)
word_dict = {}
word_list = []

for word in words:
    if word in word_dict.keys():
        word_dict[word] += 1
    else:
        word_dict[word] = 1

for word in word_dict:
    temp_list = (word, word_dict[word])
    word_list.append(temp_list)
    
word_list.sort(key = lambda x:x[1], reverse = True)

print word_list