def read_files(filename):
    try:
        with open(filename,"r") as f: 
            print(f.read())
    except FileNotFoundError:
        return "file path not found"
    except PermissionError:
        return "permission denied"
    except Exception as e:
        return e