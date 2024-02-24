import txtfile

main_folder = "user_name"
#  add all paragraph folders to this folder

num_paragraphs = 2
#  edit num_paragraphs depending on number of paragraphs in between intro and conclusion

flag = "["
#  edit the flag which calls for the replacement

keywords = {"name]": "Ben Simmons",
            "phone]": "1-800-525-0102",
            "email]": "NPIC@state.gov",
            "company]": "US Department of Defense",
            "position]": "F-22 Raptor Pilot"}


def main():
    txtfile.clear("output.txt")
    sections = ["introduction"]
    [sections.append("paragraph_"+str(i+1)) for i in range(num_paragraphs)]
    sections.append("conclusion")

    txtfile.combine(sections, main_folder, "output.txt", flag, keywords)


if __name__ == "__main__":
    main()
