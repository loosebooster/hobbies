def pad(sentence, punc):
    for p in punc:
        sentence = sentence.replace(p, " " + p + " ")
    return sentence

sentence = input("sentence: ")
punk = [".", ",", "?", "!", "'", '"', "/"]

print(pad(sentence, punk))