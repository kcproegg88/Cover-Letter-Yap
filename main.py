import os
import functions
import random

main_folder = "/user_folder"  # can edit the valid
num_paragraphs = 1
identifier = "["

def main():
    num_paragraphs = 1
    sections = ["/introduction"]
    #[sections.append("/paragraph_"+str(i)) for i in range(num_paragraphs)]
    #sections.append("/conclusion")
    for folders in sections:
        options = os.listdir(main_folder+folders)
        i = random.randint(1,len(options))
        with open(main_folder+folders+"/"+str(i)+".txt") as file:
            print(file)


if __name__ == "__main__":
    main()