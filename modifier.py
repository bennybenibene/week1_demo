def modify(x):
    """takes a string as input and joins chars with **"""

    modified_x=''

    for i,j in enumerate(x):
        if i < len(x) -1:
            modified_x += j + "----"
        else:
            modified_x += j + "----"
    
    return modified_x

def main():
    to_mod = input('Provide a string:')
    print(modify(to_mod))

if __name__ == "__main__":
    main()
