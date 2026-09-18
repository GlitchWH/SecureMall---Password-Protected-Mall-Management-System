#data fuction will be used to save data being inserted by the shop authorities
#this will save the data to txt file
#edge cases checked

filename = "MallData.txt"
def create_file():
    try:
        with open(filename, "x") as file:
            pass
    except FileExistsError:
        pass
    





