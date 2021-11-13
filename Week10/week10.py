def main():
    # # Question 1
    # print(question_1())

    # Question 2


#--------------------Question 1
# yes English sir hotel student boy love madam professor cici restaurant your excuse students are lawyer the restroom crazy my hello is man
def question_1():
    eng_sentence = input("please input an english sentence: ")
    eng_to_pirate = open_and_read_from_file_to_dict("eng2pirate")

    translated_list_sentence = []

    list_sentence = eng_sentence.split()

    # For each word in sentence that has in dict ->
    # translate to pirate and put in a list
    for word in list_sentence:
        if word in eng_to_pirate.keys():
            word = eng_to_pirate[word]
        translated_list_sentence.append(word)


    return " ".join(translated_list_sentence)



def open_and_read_from_file_to_dict(file_name):
    with open(file_name + ".txt","r") as file:
        eng_to_pirate = {}
        text = file.readlines()
        # print(text)
        for line in text:
            # print(line)
            strip_line = line.strip()
            # print(strip_line)
            words_list = strip_line.split(sep="\t")
            # print(words_list)
            # Map english words with pirate
            if len(words_list) == 3:
                eng_to_pirate[words_list[0].strip()] = words_list[2].strip()
            else:
                eng_to_pirate[words_list[0].strip()] = words_list[1].strip()

        return  eng_to_pirate

#--------------------Question 2


main()