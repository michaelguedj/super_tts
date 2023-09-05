import pyttsx3, sys, re


# test langue présente + id 
def id_language(voices, language):
    n = len(voices)
    for i in range(n):
        if language.lower() in voices[i].name.lower():
            return i
    raise TypeError('LanguageNotFound')


if __name__ == '__main__':
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    try:
        print(id_language(voices, 'hebrew'))
        print(id_language(voices, 'french'))
        print(id_language(voices, 'english'))
        print(id_language(voices, 'spanish'))
    except:
        sys.stderr.write("Language not found!\n")

    name = "toto/toto"
    if not name.endswith("/"):
        name = name+"/"
    print(name)

