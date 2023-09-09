# -*- coding: utf8 -*
import pyttsx3, sys, re, os


#--- General Usage 
if len(sys.argv) < 4:
    print("Usage: tts.py [-r |-mp3] -l [language] source_text", file=sys.stderr)
    print("Example: ", file=sys.stderr)
    print("py tts.py -mp3 -l french test_fr.txt", file=sys.stderr)
    sys.exit()

#--- Options
output_format = sys.argv[1] # [-r |-mp3]
language = sys.argv[3] # language
source = sys.argv[4] # source_text

#--- Others Usages
if not os.path.isfile(source):
    print(f"File: {source} does not exist!", file=sys.stderr)
    sys.exit()

print("Output format:", output_format)
print("Language:", language)
print("Source", source)


'''Doc : The library supports the following engines:
sapi5 - SAPI5 on Windows
nsss - NSSpeechSynthesizer on Mac OS X
espeak - eSpeak on every other platform'''
pyttsx3.init(driverName='sapi5') 


engine = pyttsx3.init()


#--- Language Option
def num_language(voices, language):
    n = len(voices)
    for i in range(n):
        if language.lower() in voices[i].name.lower():
            return i
    raise TypeError('LanguageNotFound')

voices = engine.getProperty('voices')
try:
    num = num_language(voices, language)
except:
    print("Language not found!", file=sys.stderr)
    sys.exit()

voice = engine.getProperty('voices')[num]


# language Implementation
engine.setProperty('voice', voice.id)
engine.setProperty('rate', 110) # sets speed of speech


# Concatenation of the input file into a string
f = open(source, "r", encoding="utf-8")
text = ""
lines = f.readlines()
for line in lines:
    text += line + " "
f.close()


#--- Reading option
if output_format == "-r":
    engine.say(text)


#--- MP3 saving option
if output_format == "-mp3":
    target = source.replace(".txt", ".mp3")
    print("Target:", target)
    engine.save_to_file(text, target)


engine.runAndWait()
sys.exit()
