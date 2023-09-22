def bin_go(n:int):
    for i in range(1, n+1):
        if i %3 == 0 and i % 7 == 0:
            print("bingo")
        elif i % 7 == 0:
          print("go")
        elif i % 3 == 0:
            print("bin")
        else:
            print(i)
# bin_go(100)

# Level 1 , Task 1

def reverse_integer(n: int):
    string_num = strn(n)
    return '-' + string_num[:0:-1]


print(reverse_integer(-100))


# Level 1 , Task 2

def are_anagrams(s1: str, s2: str):
    return sorted(s1) == sorted(s2)


print(are_anagrams('tub', 'but'))


# Level 2, Task 3

def reverse_words(sentence: str):
    empty_list = []
    words = sentence.split(' ')
    for word in words:
        reversed_word = words[::-1]
        empty_list.append(reversed_word)
    reversed_sentence = ''.join(reversed_word)
    return reversed_sentence


print(reverse_words("Hello my name is Zooni"))


# Level 2 , Task 4

def repeat_digits(s: str):
    result = ""
    for char in s:
        if char.isdigit():
            num = int(char)
            repeat_char = char * num
            result += repeat_char
        else:
            result += char

    return result


print(repeat_digits("D4io2p"))


# Level 2 , Task 5

def shortcut(s: str):
    result = ""
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in s:
        if char not in vowels:
            result += char

    return result


print(shortcut("assessment"))



