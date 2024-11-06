from juste_prix import *

while request != just_prize :
    count_try -= 1
    print(f"choisir un nombre entre 1 et 10000, {request}")
    request = int(input("entrer un prix: "))
    
    
    
def main():
    print("Running test 1")
    test1()
    print("Success")
    
#    print("Running test 2")
#    test2()
#    print("Success")

#    print("Running test 3")
#    test3()
#    print("success")
    

if __name__ == '__main__':
    main()    