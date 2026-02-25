import re

text=input("Enetr chat message:")
bad_words=["stupid","idiot","moral","dumb"]

pattern=r'\b(?:'+'|'.join(map(re.escape, bad_words)) + r')\b'
censored=re.sub(pattern, "***" ,text, flags=re.IGNORECASE)
print("Censored Chat: ", censored)
