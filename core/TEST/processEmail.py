from getVocabList import getVocabList
import re


def processEmail(email_contents):
    vocab_list = getVocabList()
    print(len(vocab_list))

    # process input
    email_contents = email_contents.lower()
    # email_contents = email_contents.replace("<[^<>]+>', ' ", "")
    # email_contents = re.sub("[+>', ']", "", email_contents)

    # handle numbers
    email_contents = re.sub("[0-9]+", "number", email_contents)

    # handle URL
    email_contents = re.sub("(http|https)://[^\s]*", "httpaddr", email_contents)

    email_contents = re.sub("[^\s]+@[^\s]+", "emailaddr", email_contents)
    email_contents = re.sub("[$]+", "dollar", email_contents)

    # token email
    # remove punctuations
    # @$ /  # .-:&*+=[]?!(){},''
    l = re.compile(r'@$ /  # .-:&*\+=\[]?!(){},''').split(email_contents)
    print(l)
    print(len(l))
    email_contents = re.sub(r' @$ /  # .-:&*\+=\[]?!(){},''', " ", email_contents)

    print(email_contents)



