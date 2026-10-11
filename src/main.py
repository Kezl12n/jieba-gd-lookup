
import jieba, urllib.parse, sys, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dict_path = os.path.join(BASE_DIR,  "dict", "dict.txt.big")

jieba.set_dictionary(dict_path)

if len(sys.argv) < 2:
    print("Error: Add a text string.")
    sys.exit(1)

text = sys.argv[1]


# Search text

sent = jieba.lcut_for_search(text)


## Remove punctations/symbols

clean_sent = [l for l in sent if l.isalnum()]



def html_parser(input_text):
   
    # Array for seperating words
    links = []
    for char in input_text:
        
        char = char.strip()
        if not char:
            continue
        
        encoded = urllib.parse.quote(char)

        link = f'<a href="gdlookup://localhost/{encoded}" style="text-decoration:none;color:blue;">{char}</a>'
        links.append(link)

    body = " / ".join(links)
    return f'<div style="font-size: 40px; line-height: 1.8;">{body}</div>'


    

result = html_parser(clean_sent)

output = sys.stdout.buffer.write(result.encode('utf-8'))




