count_the = 0
with open("gutenberg.txt",encoding="UTF-8") as file_obj:
    for line in file_obj:
        count_the += line.strip().lower().count("the")

count_the_sp = 0
with open("gutenberg.txt",encoding="UTF-8") as file_obj:
    for line in file_obj:
        count_the_sp += line.strip().lower().count("the ")

print(f"Count of words in which 'the' appears: {count_the}")
print(f"Count of words in which 'the ' appears: {count_the_sp}")