def write_number_to_file(filename):
    try:
        with open(filename,"w") as file:
            for i in range(1,101):
                file.write(str(i)+"\n")

    except FileNotFoundError:
        return "file path not found"
    except PermissionError:
        return "permission denied"
    except Exception as e:
        return e