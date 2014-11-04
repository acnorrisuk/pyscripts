# keyword arguments and default parameter values

# positional parameters

def birthday1(name, age):
    print("Happy Birthday,", name,"!", "I head you're", age, "today\n")

# default parameters

def birthday2(name = "Jeremy", age = "6"):
    print("Happy Birthday,", name,"!", "I head you're", age, "today\n")

birthday1("Bob", "105")

birthday2()

birthday2("Katherine", "27")

input("exit")
