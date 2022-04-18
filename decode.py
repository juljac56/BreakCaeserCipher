from encode import encode

def decode(word):
    
    if word:
        output = []
        
        for key in range(0,26):
            output.append(encode(word, key))
        return output

