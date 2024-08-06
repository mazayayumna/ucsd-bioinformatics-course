def pattern_count(text, pattern):
    count = 0
    text = text.strip()
    pattern_strip = pattern.strip()
    for i in range(len(text)):
        if text[i:len(pattern_strip)+i] == pattern:
            count = count + 1
    return count

lines = open('./dataset/count_pattern.txt').read().split("\n")
count = pattern_count(lines[0], lines[1])
print(count)

word_list = []
count_dict = {}
def frequent_words(text, kmer):
    text_strip = text.strip()
    for i in range(len(text_strip)):
        word = text[i:kmer+i]
        word_list.append(word)

    for w in word_list:
        if w in count_dict:
            count_dict[w] +=1
        else:
            count_dict[w] = 1
    
    max_count = max(count_dict.values())
    most_common_strings = [string for string, count in count_dict.items() if count == max_count]
    freq_word = ' '.join(s.strip() for s in most_common_strings)
    return freq_word

lines2 = open('./dataset/freq_words.txt').read().split("\n")
freq = frequent_words(lines2[0], int(lines2[1]))
print(freq)
