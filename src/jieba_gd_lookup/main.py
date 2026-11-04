
import jieba, urllib.parse, sys, os, argparse



def run():
    # Initialize arg
    parser = argparse.ArgumentParser(description="Options for parsing sentences.")

    # Define args
    parser.add_argument("-i", "--index", action="store_true", help="Use search mode for indexing sub-words")
    parser.add_argument("-m", "--mono", action="store_true", help="Parse and split by single character while disregarding two character compounds.")
    parser.add_argument("-d", "--dict", type=str, help="Select main dictionary.")
    parser.add_argument("-u", "--user_dict", type=str, help="Select user dictionary.")
    parser.add_argument("text", type=str, nargs="?", default="", help="Input text to parse.")
 
    args = parser.parse_args()

    # Dictionary
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    dict_path = os.path.join(BASE_DIR,  "dict", "dict.txt.big")

    jieba.set_dictionary(dict_path)

    if args.dict is not None:
        if os.path.exists(args.dict):
            jieba.set_dictionary(args.dict)
        else:
            print(f"Error: Preferred main dictionary not found at {args.dict}. Falling back to default big dict.", file=sys.stderr)
            jieba.set_dictionary(dict_path)

    if args.user_dict is not None:
        cleaned_path = args.user_dict.strip()

        if not cleaned_path:
            raise ValueError("Error: User dictionary path cannot be empty.")

        if os.path.exists(cleaned_path):
            jieba.load.userdict(cleaned_path)
        else:
            print(f"""
              <div style="padding: 15px; background-color: #ffebee; border: 1px solid #f44336; border-radius: 4px; color: #c62828; font-family: sans-serif;">
                <strong>⚠️ Dictionary Loading Error:</strong><br>
                User dictionary file not found at: <code>{args.user_dict}</code>.<br>
                Please check your path.
             </div>
            """)

            raise FileNotFoundError(f"User dictionary missing: {cleaned_path}")
             
	   

    # Selected text
    text = args.text

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
 


