def get_word_count(contents):
    num_words = len(contents.split())
    return num_words
    

def get_letter_counts(contents):
    l_contents = contents.lower()
    alpha_dict = { }
    for c in range(0, len(l_contents)):
        if l_contents[c] in alpha_dict:
           alpha_dict[l_contents[c]] += 1
        else:
            alpha_dict[l_contents[c]] = 1
    return alpha_dict

def sort_dict(to_sort):
    expand_dict = []
    for char in to_sort:
        expand_dict.append({"name": char, "count": to_sort[char]})

    expand_dict.sort(reverse=True, key=sort_on)
    return expand_dict

def sort_on(dict):
    return dict["count"]

def print_book_stats_report(word_count, letter_count, file_path):
    p_dict = sort_dict(letter_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for y in range(0, len(p_dict)):
        if p_dict[y]["name"].isalpha():
            print(f"{p_dict[y]["name"]}: {p_dict[y]["count"]}")
    print("============= END ===============")