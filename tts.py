# -*- coding: utf8 -*
import pyttsx3
import sys


#--- Usage
if len(sys.argv) < 4:
    print('Usage: tts.py [-r |-mp3] -l [fr | en | hb] source_text', file=sys.stderr)
    print('Example: ', file=sys.stderr)
    print('py tts.py -mp3 -l fr text2.txt', file=sys.stderr)
    sys.exit()


#--- Options
output_format = sys.argv[1] # [-r |-mp3]
language = sys.argv[3] # [fr | en]
source = sys.argv[4] # source_text

print("Output format:", output_format)
print("Language:", language)
print("Source", source)


'''Doc : The library supports the following engines:
sapi5 - SAPI5 on Windows
nsss - NSSpeechSynthesizer on Mac OS X
espeak - eSpeak on every other platform'''
pyttsx3.init(driverName='sapi5') 


engine = pyttsx3.init()


#--- Language option
if language == "fr":
    voice = engine.getProperty('voices')[3]

if language == "en":
    voice = engine.getProperty('voices')[0]

if language == "hb":
    voice = engine.getProperty('voices')[1]


# language implementation
engine.setProperty('voice', voice.id)
engine.setProperty('rate', 110) # sets speed of speech


# concatenation of the input file into a string
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
