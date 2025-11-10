#WAF to print the elements of a list in a single line.(list is the parameter)

cities=["delhi","gurgaon","noida","pune","mumbai","chennai"]
heroes=["thor","ironman","captain america","shaktiman"]

print(heroes[0], end="\n")
print(heroes[1], end="\n")

def print_len(list):
    print(len(list))


print_len(cities)
print_len(heroes)
