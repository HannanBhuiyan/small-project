with open('demo.txt', 'r') as r_file:
    all_words = []
    for line in r_file.readlines():
          word = line.strip().split(" ")
          all_words += word

    unique_words = set(all_words)
    sorted_words = sorted(unique_words)

    with open('unique.txt', 'w') as write_file:
        for w_line in sorted_words:
             write_file.write(w_line)
             write_file.write('\n')

print("Program End\n")
