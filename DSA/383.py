#!/usr/bin/env python3

def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        res = False
    
        if len(magazine) < len(ransomNote):
            return res
    
        # fill dict with magazine
        dct = {}
        for i in magazine:
            if i not in dct:
                dct[i] = 0
            if i in dct:
                dct[i] += 1
            # dct[i] = dct.get(i, 0) + 1
                
        # go through ransomNote
        for i in ransomNote:
            # if letter is in the dictionary, substract 1
            if i in dct:
                dct[i] -= 1
            if i not in dct or dct[i] < 0:
                return res
        
        return True

''' 

other solution:

def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    for letter in list(set(ransomNote)):
        if ransomNote.count(letter) > magazine.count(letter):
            return False
    return True

'''
        
def main():
    ransomNote = "aa"
    magazine = "aab"
    
    res = False
    
    if len(magazine) < len(ransomNote):
        return res
    
    dict = {}
    for i in magazine:
        if i not in dict:
            dict[i] = 0
        if i in dict:
            dict[i] += 1
    
    print(f"dict before op: {dict}")

    for key in ransomNote:
        # if letter is in the dictionary, substract 1
        if key in dict:
            dict[key] -= 1
        if key not in dict or dict[key] < 0:
            print("not enough letter") 
        
            
        
        
    print(f"dict after op: {dict}")

    


if __name__ == "__main__":
    main()