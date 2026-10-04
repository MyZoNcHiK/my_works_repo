def open_file(filename):
    try:
        file = open(filename, "r")
        print("Ok")
        file.close()
    except IOError:
        print("Зловили I/O error")
    finally:
        print("Done")

filename = input()
open_file(filename)
