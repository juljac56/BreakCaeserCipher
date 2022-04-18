




def encode(word, key):
    
    if word and key:
        word = word.lower()
        key = key%26
        output = []
        
        for letter in word:
            
            nb = ord(letter)
            
            if nb < 97 or nb > 122 :
                output.append(letter)
            else:
                relatif_nb = nb-97
                new_nb = (relatif_nb + key)%26
                output.append(chr(new_nb+97))
                
        return ''.join(str(e) for e in output)
    
