import re
text = input()
print(re.split('<span>|,|&nbsp', text))
new_text = re.split('<span>|,|&nbsp', text)
print(new_text[1] + new_text[2])
number = int(new_text[1] + new_text[2])
print(number + 1)