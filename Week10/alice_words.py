from collections import OrderedDict

stop_word_list = ["`",".",",",";","!","\"","?","(",")"]

def main():
    # print(is_apostrophe_between("joined):"))

    # print(is_hyphen_between("joined):"))

    # print(generate_word_list_from_file("alice"))

    # print(is_double_hyphen_consecutively("joined):"))


    # print(filter_word("knew)"))

    # print(filter_word_list(["joined):"]))

    # print(delete_apostrophe_at_the_end("word's'"))

    question_2()



def question_2():
    raw_word_list_from_file = generate_word_list_from_file("alice")
    filtered_word_list = filter_word_list(raw_word_list_from_file)
    word_freq_dict = count_word_freq(filtered_word_list)

    ordered_word_freq = OrderedDict(word_freq_dict)

    for key in sorted(ordered_word_freq):
        ordered_word_freq.move_to_end(key)

    # print(ordered_word_freq)

    write_to_file(ordered_word_freq)

    # How many times does the word Alice occur in the book?
    print("The word Alice appear in the text for", ordered_word_freq.get("alice"),"times")

    # What is the longest word in the book?
    print("the longest word is",find_longest_word_in_dict(ordered_word_freq))

    # How many characters does the longest word have?
    print("the longest word has",len(find_longest_word_in_dict(ordered_word_freq)),"characters")

def write_to_file(word_freq):
    with open("alice_words.txt", "w+") as file:
        word = "Word"
        count = "Count"
        file.write(f'{word:<30}{count}' + "\n")
        for w,c in word_freq.items():
            file.write(f'{w:<30}{c}' + "\n")

def is_alphabet(char):
    return ord(char) in range (ord("a"),ord("z")+1)

def generate_word_list_from_file(file_name):
    with open( file_name+ ".txt","r") as file:
        text = file.readlines()
        word_list = []
        # print(text)
        for line in text:
            # print(line)
            strip_line = line.strip()
            # print(strip_line)
            word_sentence_list = strip_line.split(sep=" ")

            # print(word_list)
            for word in word_sentence_list:
                word_list.append(word.lower())
        return word_list

def filter_word_list(word_list):
    filtered_word_list = []
    for word in word_list:
        # Case if word is empty
        if len(word) == 0:
            continue
        # Case double hyphen consecutively
        elif is_double_hyphen_consecutively(word):
            new_word_list = word.split(sep='--')
            for each_word in new_word_list:
                if len(each_word) > 0:
                    if is_hyphen_between(each_word) or is_apostrophe_between(each_word):
                        # print(delete_stop_word(each_word))
                        filtered_word_list.append(delete_stop_word(each_word))
                    else:
                        if len(filter_word(each_word)) > 0:
                            filtered_word_list.append(filter_word(each_word))

        # Case apostrophe or hyphen between
        elif is_hyphen_between(word) or is_apostrophe_between(word):
            delete_stop = delete_stop_word(word)
            # print(delete_apostrophe_at_the_end(delete_stop))
            filtered_word_list.append(delete_apostrophe_at_the_end(delete_stop))
        # Other case: for example: "axe."; "'bat"
        else:
            if len(filter_word(word)) > 0:
                # print(filter_word(word))
                filtered_word_list.append(filter_word(word))


    return filtered_word_list

def filter_word(word):
    filtered_word = ""
    for char in word:
        if is_alphabet(char):
            filtered_word += char
    return filtered_word


def is_apostrophe_between(word):
    for index in range(len(word)):
        try:
            if word[index] == "'" and index - 1 < 0:
                return False
            if word[index] == "'" and is_alphabet(word[index+1]) and is_alphabet(word[index-1]):
                return True
        except IndexError:
            return False
    return False

def is_hyphen_between(word):
    for index in range(len(word)):
        try:
            if word[index] == "-" and index - 1 < 0:
                return False
            if word[index] == "-" and is_alphabet(word[index+1]) and is_alphabet(word[index-1]):
                return True
        except IndexError:
            return False
    return False

def is_double_hyphen_consecutively(word):
    for index in range(len(word)):
        try:
            if word[index] == "-" and word[index+1] == "-":
                return True
        except Exception:
            return False
    return False

def count_word_freq(word_list):
    word_list_dict = {}
    for word in word_list:
        if word in word_list_dict:
            word_list_dict[word] += 1
        else:
            word_list_dict[word] = 1
    return word_list_dict

def delete_stop_word(word):
    new_word = ""
    for char in word:
        if char in stop_word_list:
            continue
        new_word += char
    return new_word

def delete_apostrophe_at_the_end(word):
        if word[len(word)-1] == "'":
            word = word[:len(word)  - 1]
        return word


def find_longest_word_in_dict(word_dict):
    maximum_length = 0
    longest_word = ""
    for word in word_dict:
        if maximum_length < len(word):
            maximum_length = len(word)
            longest_word = word
    return longest_word

main()