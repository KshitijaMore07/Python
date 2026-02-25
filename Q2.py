def count_vowels(s):
    vowels="aeiou"
    s=s.lower()
    count=0
    for char in s:
        if char in vowels:
            count+=1
        return count
    print(count_vowels("Hello world"))
