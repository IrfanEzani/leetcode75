from typing import List

def compress(chars: List[str]) -> int:
    i = 0
    count = 1
    for j in range(1, len(chars)+1):
        if j < len(chars) and chars[j] == chars[j-1]:
            count += 1
        else:
            chars[i] = chars[j-1]
            i += 1
            if count > 1:
                for k in str(count):
                    #print(f"i: {i}, k: {k}, chars[i]: {chars[i]}")
                    chars[i] = k
                    i += 1
            count = 1
    return i

def main():
    print(compress(["a","a","b","b","c","c","c"]))
    
if __name__ == '__main__':
    main()