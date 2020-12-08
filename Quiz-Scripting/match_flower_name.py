# HINT: create a dictionary from flowers.txt
def build_flower_dictionary(path_to_file):
    with open(path_to_file) as f:
        flowers = {}
        for line in f:
            key_value = tuple(line.split(":"))
            flowers[key_value[0]] = key_value[1].strip()
    return flowers

# HINT: create a function to ask for user's first and last name
def get_name():
    return input("Enter your First [space] Last name only: ")

# print the desired output
def main():
    name = get_name()
    flower_dict = build_flower_dictionary("flowers.txt")
    BOLD = '\033[1m'
    END = '\033[0m'
    print("Unique flower name {}with the first{} letter: {}".format(BOLD, END, flower_dict[name.capitalize()[0]]))

if __name__ == "__main__":
    main()