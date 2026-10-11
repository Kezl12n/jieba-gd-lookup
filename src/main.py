
import jieba, urllib.parse, sys, os, argparse


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dict_path = os.path.join(BASE_DIR,  "dict", "dict.txt.big")

jieba.set_dictionary(dict_path)

if len(sys.argv) < 2:
    print("Error: Add a text string.")
    sys.exit(1)

text = sys.argv[1]

# Initialize arg
parser = argparse.ArgumentParser(description="Options for parsing sentences.")

# Define args
parser.add_argument("text", type=str, nargs="?", default="", help="Input text to parse.")

parser.add_argument("-i", "--index", action="store_true", help="Use search mode for indexing sub-words")

parser.add_argument("-m", "--mono", action="store_true", help="Parse and split by single character while disregarding two character compounds.")

args = parser.parse_args()



# Default: accurate mode (akin to parsing sentences)
sent = jieba.lcut(text)

if args.index:
   sent = jieba.lcut_for_search(text)

if args.mono:
   sent = jieba.lcut(" ".join(text))


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

    body = " ".join(links)

    # Triple quotes = ignore single or double quotes inside the string
    return f"""<div style="font-size: 40px; line-height: 1.8; font-family: system-ui, 'Noto Sans CJK SC', 'Noto Sans CJK TC', sans-serif;">{body}</div>"""


result = html_parser(clean_sent)

output = sys.stdout.buffer.write(result.encode('utf-8'))




