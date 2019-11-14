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
                list_directory = file_name.split("/")
                full_curr_file_name = list_directory[len(list_directory) - 1]
                new_file_name = full_curr_file_name[:full_curr_file_name.rfind(".")] \
                                + str(file_number) \
                                + full_curr_file_name[full_curr_file_name.rfind("."):]
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


copy_file("./ca.che.txt")
copy_file("cache.txt")
# copy_file("cache.txt", "test.txt")
