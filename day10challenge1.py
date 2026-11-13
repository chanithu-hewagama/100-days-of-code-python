def format_name(f_name, l_name):
    f_name = f_name.lower()
    l_name = l_name.lower()
    letters_f_name = []
    for each in f_name:
        letters_f_name.append(each)
    letters_l_name = []
    for each in l_name:
        letters_l_name.append(each)
    letters_f_name[0] = letters_f_name[0].upper()
    letters_l_name[0] = letters_l_name[0].upper()
    f_name = ""
    l_name = ""
    for each in letters_f_name:
        f_name += each
    for each in letters_l_name:
        l_name += each

    return f_name + " " + l_name

def main():

    print(format_name("cHaNiThU", "HeWaGaMa"))

if __name__ == '__main__':
    main()