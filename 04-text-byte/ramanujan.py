import re

re_numbers_str = re.compile(r'\d+')
re_words_str = re.compile(r'\w+')
re_numbers_bytes = re.compile(rb'\d+')
re_words_bytes = re.compile(rb'\w+')

text_str = ("Ramanujan saw \u0be7\u0bed\u0be8\u0bef"  
            " as 1729 = 1³ + 12³ = 9³ + 10³.")
text_bytes = text_str.encode('utf_8')

print('Text', repr(text_str), sep='\n ')
print('Numbers')
print('   str  :', re_numbers_str.finditer(text_str))
print('   bytes:', re_numbers_bytes.finditer(text_bytes))
print('Words')
print('   str:', re_words_str.finditer(text_str))
print('   bytes:', re_words_bytes.finditer(text_bytes))
