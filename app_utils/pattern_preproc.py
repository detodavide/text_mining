import re

def clean_text(text, patterns):

    for pattern, replacement in patterns.items():
        text = re.sub(pattern, replacement, text)
    text = text.lower().strip()
    return [text]

def preprocess(input):

    patterns = {
                r"UTC]": '',
                r"b'": '',
                r'\d+': '',      
                r'[^\w\s]': '',  
                r'\b\w{1,2}\b':'',
                r'(http|www)[^\s]+':'',
                r' said ': '', 
                r' say ': '',
                r' one ': '',
                r'\s+': ' '   
                }
    
    if isinstance(input, str):
        cleaned_text = clean_text(input, patterns)
        return cleaned_text
