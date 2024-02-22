import txtfile

main_folder = "user_name"  # can edit the foldername
num_paragraphs = 1
flag = "["
keywords = {"name]": "your name", "company]": "github", "position]": "Software Engineer"}

def main():
    num_paragraphs = 2
    sections = ["introduction"]
    [sections.append("paragraph_"+str(i+1)) for i in range(num_paragraphs)]
    sections.append("conclusion")

    txtfile.combine(sections, main_folder, "output.txt", flag, keywords)

    input()
    txtfile.clear("output.txt")


if __name__ == "__main__":
    main()