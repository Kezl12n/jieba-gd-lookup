
import jieba, urllib.parse

jieba.set_dictionary('dict/dict.txt.big')

text = "这是一个没有字典的例子"

# Search text

sent = jieba.lcut_for_search(text)


## Remove punctations/symbols

clean_sent = [l for l in sent if l.isalnum()]

def html_parser(input_text):
    output = '<div style="font-size: 20px; line-height: 1.8;">'

    for char in input_text:
        if char.isspace():
            output += " "
            continue
        
        encoded = urllib.parse.quote(char)

        output += f'<a href="gdlookup://localhost?word={encoded}" style="text-decoration:none;color:blue;">{char}</a>'

    output += '</div>'
    return output

print(html_parser(clean_sent))
