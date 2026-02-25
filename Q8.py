import re
sentence=input("Enter a sentence:")
result=re.sub(r'\b(\w+)(\1\b)+',r'\1', sentence)

print("After removing duplicates:",result)
