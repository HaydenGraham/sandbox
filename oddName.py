""" Hayden """
def main():

    freq = int(input("What frequency of letters would you like to print? "))

    name = get_name()
    print_every_nth_letter(name, freq)

def get_name():
    try:
     name = str(input("Insert name:   "))
     while len(name) == 0:
         name = input("Insert name:  ")


    except ValueError:
        print("Enter a valid number")
    return name



def print_every_nth_letter(name,freq):
    for i in range(0, len(name), freq):
        print(name[i])


main()
