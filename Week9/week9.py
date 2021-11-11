def main():
    # # Question 1
    # question_1()

    # # Question2
    # question_2()

    # # Question 3
    # question_3()

    # Question 4
    question_4()

#-------------- Question 1
def question_1():
    messages = input("input your messages: ")
    with open("messages.txt","w+") as question1:
        for index in range(1,101):
            question1.write(str(index) + ". " + messages+"\n\n")

#-------------- Question 2
def question_2():
    file_name = input("input your file name: ")
    with open(file_name+".txt","w+") as question2:
        circle = open("turtle_file.py","r")
        readed_circle = circle.read()
        question2.write(str(readed_circle))
        circle.close()


#-------------- Question 3
def question_3():
    existed_file = input("enter the name of the file you want to open: ")
    create_a_new_file_based_on_existing_file(existed_file)

def create_a_new_file_based_on_existing_file(existed_file_name):
    with open("new_"+existed_file_name+".txt","w+") as new_file:
        existed_file = open_existed_file(existed_file_name)
        for index in range(1,len(existed_file)):
            new_file.writelines(str(index) + ". " + existed_file[index-1])



def open_existed_file(existed_file_name):
    with open(existed_file_name+".txt","r") as existed_file:
        return existed_file.readlines()

#-------------- Question 4
def question_4():
    # In programming the beginning index is 0, but in reality, for the file instance, it is 1
    # So have to plus one to get the correct line and correct index in file
    with open("edited_vietnam.txt","r") as edited_vietnam:
        edited_vietnam_list = edited_vietnam.readlines()
        for first_index in range(1, len(edited_vietnam_list)):
            # print(edited_vietnam_list[index])
            split_text_list = edited_vietnam_list[first_index].split(sep=",")
            for second_index in range(len(split_text_list)):
                if split_text_list[second_index] == "":
                    print("line",first_index+1,"missing values at index", second_index+1)



main()