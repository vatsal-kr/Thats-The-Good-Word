def isplural(word):
  singular = wnl.lemmatize(word, 'n')
  return singular!=word

def ttgw(word1, word2, word3):
  similar_words = model.most_similar(word1, topn=1000)
  starting=""
  ending=""
  
  if(word2 in exceptions_prefix_dct.keys()):
    starting+=exceptions_prefix_dct[word2]
  elif(isplural(word2)):
    starting+=(word2[0]+word2[2])
  else:
    starting+=(word2[0]+word2[1])
  if(isplural(word3)):
    starting+=(word3[0]+word3[2])
  else:
    starting+=(word3[0]+word3[1])
  similar_words = [word[0] for word in similar_words if word[0].startswith(starting)]
  return similar_words
