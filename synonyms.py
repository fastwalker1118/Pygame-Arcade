import copy
import re


def cosine_similarity(vec1, vec2):
    a = 0
    b = 0
    c = 0
    for word in vec1.keys():
        if word in vec2:
            a = a + vec1[word] * vec2[word]
        else:
            a = a
    for value in vec1.values():
        b = b + value**2
    for value in vec2.values():
        c = c + value**2
    a = a / (b**0.5 * c**0.5)
    return a

#given an individual 1d array from 2d sentence, update dictionary
def updatedic(sentences1d, dic):
    sentences1d_2 = list(dict.fromkeys(sentences1d))
    for i in range(len(sentences1d_2)):
        for j in range(len(sentences1d)):
            if sentences1d_2[i] != sentences1d[j]:
                word1 = sentences1d[i]
                word2 = sentences1d[j]
                if word1 not in dic.keys():
                    dic[word1] = {}
                val = 0
                if word2 in dic[word1].keys():
                    val = dic[word1][word2]
                dic[word1][word2] = val + 1
    return dic

def build_semantic_descriptors(sentences):
    dict = {}
    for i in range(len(sentences)):
        dict = updatedic(sentences[i], dict)
    #print(dict)
    return dict

def tokenize_sentences(text):
    sentences = re.split(r"[.!?]+", text)
    sentences_processed = []
    for sent in sentences:
        strip_sent = sent.strip()
        if strip_sent:
            sentences_processed.append(strip_sent)
    return sentences_processed

def build_semantic_descriptors_from_files(filenames):
    all_sentences = []
    final_output = []
    for filename in filenames:
        with open(filename, "r", encoding="latin1") as file:
            file_content = file.read()
        sentences = tokenize_sentences(file_content)
        for sent in sentences:
            a = re.split('\W+', sent)
            all_sentences.append(a)
        for sent in all_sentences:
            res = []
            for word in sent:
                word = word.lower()
                res.append(word.replace("\n", ""))
            sent = res
            final_output.append(sent)
        #print(final_output)
    semantic_descriptors = build_semantic_descriptors(final_output)
    #print(semantic_descriptors)
    return semantic_descriptors

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    vec1 = semantic_descriptors[word]
    word_choice = ""
    highest = -1
    for words in choices:
        vec2 = semantic_descriptors[words]
        if cosine_similarity(vec1, vec2) > highest:
            highest = cosine_similarity(vec1, vec2)
            word_choice = words
    return word_choice

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    file = open(filename, "r", encoding="latin1")
    Lines = file.readlines()
    correct = 0
    for lines in Lines:
        line = lines.split()
        #print(line)
        #print(line[2:])
        word = most_similar_word(line[0], line[2:], semantic_descriptors, similarity_fn)
        if line[1] == word:
            correct += 1
        #print(line[0], " ", word)
    return correct/len(Lines)*100

if __name__ == "__main__":
    sem_descriptors = build_semantic_descriptors_from_files(["book.txt", "book2.txt"]) #
    #print("1")
    res = run_similarity_test("txt.txt", sem_descriptors, cosine_similarity)
    print(res, "of the guesses were correct")







    