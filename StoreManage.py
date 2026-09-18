#here in this function the user will insert all about the product
#and whole data about product will be saved 
filename = "Products.txt"
def add_p():
    print("Enter product details...")
    p_name = input("Enter product name: ")
    p_price = input("Enter product price: ")
    p_price = int (p_price)
    p_brand = input("Brand name: ")
    p_quantity = input("Quantity of Product: ")

  
    try:
        with open(filename, "x") as file:
            pass
    except FileExistsError:
        pass

    with open(filename, "a") as file:
        file.write(f"***** Product *****\n Name: {p_name}\n Price: {p_price}/-PKR\n Brand: {p_brand}\n Quantity: {p_quantity}\n")

    print("Item Added successfully...")        

def check_all_products():
    with open(filename, "r") as file:
        show_p = file.read()
        print(show_p)
