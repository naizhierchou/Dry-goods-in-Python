def m2():
     f = open("output.txt", "w")
     try:
        f.write("python之禅")
     except IOError:
        print("oops error")
     finally:
        f.close()