def getVocabList():
    # open file
    list_of_lists = []
    vocabList = []

    with open('data/vocab.txt') as f:
        for line in f:
            inner_list = [elt.strip() for elt in line.split('\t')]
            list_of_lists.append(inner_list)

    # number of features
    noFeatures = 1899
    
    # print(list_of_lists)
    for i in list_of_lists:
        vocabList.append(i[1])
    return vocabList
