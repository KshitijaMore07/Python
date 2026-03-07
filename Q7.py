with open("demo.pdf","rb")as f1, open("demo.pdf","wb")as f2:
    f2.write(f1.read())
print("Binary file copied successfully.")
