import re
text = "Ala ! maaa, kota. X D"
text = re.split('[,.!]', text)
print(text)
