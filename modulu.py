from packets.modul import samitler  

def samitler(cumle):
    vowels = ["A", "I", "O", "U", "E"]
    newlist = []
    
    for i in cumle: 
        is_vowel = False
        for j in vowels:
            if i.upper() == j:
                is_vowel = True
                break
        if not is_vowel:
            if i not in newlist and i != " ":
                newlist.append(i)
    
    return newlist


a = input("Bir cümle girin: ")
yeni = samitler(a)

print(yeni)
