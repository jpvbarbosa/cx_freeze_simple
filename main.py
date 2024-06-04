from package1 import module1

def test():

    print ("Hello from test!")

if __name__ == "__main__":

    test()
    module1.test()
    print ("Hello from main!")
    input("Press Enter to continue...")