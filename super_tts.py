import os, shutil, re, sys


#--- Usage
if len(sys.argv) < 3:
    print('Usage: super_tts.py -l [fr | en] source_folder', \
          file=sys.stderr)
    print('Example: ', file=sys.stderr)
    print('py super_tts.py -l fr test/', file=sys.stderr)
    sys.exit()


#--- Options
language = sys.argv[2] # [fr | en]
source_folder = sys.argv[3] # source_folder

print("Language:", language)
print("Source folder:", source_folder)


# generation of a list contenaing the text source (of extension ".txt")
text_sources = []
entries = os.listdir(source_folder)
for entry in entries:
        match = re.search("\.txt$", entry)
        if match:
            text_sources.append(entry)


#--- Target folder
target_folder = source_folder.replace("/", "_")
target_folder = target_folder.replace("\\", "_")
target_folder = target_folder+"_mp3"
print(target_folder)

if os.path.exists(target_folder):
    shutil.rmtree(target_folder)

os.mkdir(target_folder)
        
os.chdir(target_folder)

for entry in text_sources:
    input_file = "../" + source_folder + entry
    print(f"py ../tts.py -mp3 -l fr {input_file}")
    os.system(f"py ../tts.py -mp3 -l fr {input_file}")
    output_file = input_file.replace(".txt", ".mp3")
    shutil.move(output_file, ".")

