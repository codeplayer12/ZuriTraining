def read_file_content(filename):
    with open(filename,"r") as f:
        contents = f.read().lower().split()
    return contents


def count_words():
    text = read_file_content("./story.txt")
    my_set = set(text)
    my_dict = {}
    for i in my_set:
        my_dict[i] = text.count(i)
    return my_dict
    


print(count_words())