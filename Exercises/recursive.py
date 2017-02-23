def char_count(s, c):
    if s:
        return (1 if s[0] == c else 0) + char_count(s[1:], c)
    else:
        return 0


print(char_count('hello', 'l'))
