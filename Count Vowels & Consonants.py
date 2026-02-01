def count(str):
    vowel = 0
    cons = 0
    for char in str:
        if char in ["a","e","i","o","u"] or char in ["A","E","I","O","U"]:
            vowel += 1
        elif char == " ":
            continue
        else:
            cons += 1
    data = [vowel, cons]
    return data

sen = input("Enter a sentence: ")
data = count(sen);
print("Number of Vowels:",data[0])
print("Number of Consonants:",data[1])