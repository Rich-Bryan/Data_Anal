def exist(letter):
    arr = ["A","B","C","D"]
    letter = letter.upper()

    if letter in arr:
        return True
    return False

print(exist("C"))


def c_word(paragraph, s_word):
    count = 0
    arr = paragraph.split()
    for word in arr:
        if s_word == word:
            count+=1

    return count

def c_sentences(sentences):
    count = 0
    arr = sentences.split(".")
    print(arr)
    for word in arr:
        count += 1
    return count-1

   

print(c_word("the temple the hello the yerr", "temple"))
print(c_sentences("the temple the hello the yerr. fjdklasflidsjfa. fjdklasjfd."))
word = "the temple the hello the yerr. fjdklasflidsjfa. fjdklasjfd."
print(word.count("temple"))









def calculateAverageNumberOfWordsPerSentence(textFile):
    total_words = 0
    sentence_count = 0
    with open(textFile, "r") as file:
            for line in file:
                    sentences = line.split()
                    sentence_count += 1
                    for sentence in sentences:
                            print(sentence)
                            word_count = len(sentence.split()) # make a word in an array and get the len of array
                            total_words += word_count
                                

    print(total_words)
    print(sentence_count)

    average_words = total_words / sentence_count 
    
    return average_words