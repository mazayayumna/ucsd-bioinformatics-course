def reverse_complement(pattern):
   reversed_string = pattern[::-1]
   trans_table = str.maketrans('ATCG', 'TAGC')
   rev_comp = reversed_string.translate(trans_table)
   return rev_comp

lines = open('./dataset/reverse_complement.txt').read()
rc = reverse_complement(lines)
print(rc)

loc_list = []
def pattern_matching(pattern, text):
   text = text.strip()
   pattern_strip = pattern.strip()
   for i in range(len(text)):
      if text[i:len(pattern_strip)+i] == pattern:
         loc_list.append(str(i))
   return loc_list

lines2 = open('./dataset/Vibrio_cholerae.txt').read().split("\n")
loc = pattern_matching("CTTGATCAT", lines2[0])
loc = ' '.join(l.strip() for l in loc)
print(loc)
