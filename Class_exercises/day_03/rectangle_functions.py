
def display(data):
    print(f"the area is {data}")

def get_input():
    length_asked = input("length :")
    width_asked = input("width :")
    
    return(length_asked, width_asked)

def compute_area(length,width):
    area= int(length) * int(width)
    return area

def main():
    (length, width) = get_input()

    area = compute_area(length, width)
    display(area)

main()