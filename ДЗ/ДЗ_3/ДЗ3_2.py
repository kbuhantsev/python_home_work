def copy_file(file_name="", copy_name=None):
    try:
        input_file = open(file_name, "r")
    except FileNotFoundError:
        print("Не удалось открыть входной файл!")
        return False

    if copy_name is None:
        file_number = 1
        while True:
            try:
                new_file_name = file_name.split(".")[0] + str(file_number) \
                                + "." + file_name.split(".")[1]
                output_file = open(new_file_name)
            except FileNotFoundError:
                copy_name = new_file_name
                break
            file_number += 1

    try:
        output_file = open(copy_name, "w")
        for line in input_file:
            output_file.write(line)
        output_file.flush()
    except FileNotFoundError:
        print("Не удалось найти файл назначения!")
        return False
    finally:
        output_file.close()

    return True


copy_file("cache.txt")
copy_file("cache.txt", "test.txt")
