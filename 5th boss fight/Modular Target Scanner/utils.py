def read_targets(filename):
    try : 
        with open(filename , "r") as file :
            return file.read().splitlines()
    except FileNotFoundError :
        print("Invalid File.")
        return []
