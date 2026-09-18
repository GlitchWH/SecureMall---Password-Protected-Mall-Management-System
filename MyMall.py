
from security_check import security_check
from StoreManage import add_p
from StoreManage import check_all_products
from trending_products import trend_p
from security_check import show_verif
from security_check import show_p_check

#main menue(for the mall)
print("     === { Welcome to EmberSky shopping mall } ===")
print("Please note:     This pannel is only for Administration use")
print()
print("""
1.Add new product
2.Check available products
3.Trending Products
4.Exit
""")


while(True):
    #choice match cases
    choice = input("Enter Number (1-4): ")
    choice = int(choice)
    match choice:
        case 1:
            show_verif()
            security_check()
            add_p()
            
        case 2:
            show_p_check()
            security_check()
            check_all_products()
            
        case 3:
            trend_p()
            
        case 4:
            exit()

