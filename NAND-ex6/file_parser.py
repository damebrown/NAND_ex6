import os


def directory_parser(path):
    """
    parses the input the program has got into an array of absolute paths of files to work with
    :param path: the input path
    :return: a list of absolute paths of files to work with
    """
    if os.path.isdir(path):
        path_array, valid_paths = os.listdir(path), []
        for index, dir_path in enumerate(path_array):
            dir_path = os.path.abspath(os.path.sep.join([path, dir_path]))
            if dir_path.endswith(".asm") and not os.path.isdir(
                    path_array[index]):
                valid_paths.append(dir_path)
        return valid_paths
    else:
        return [path]


def clean_empty(lines_array):
    """
    cleans empty lines from the .asm files
    :param lines_array: the array of lines to clean
    :return: the clean array
    """
    for line in lines_array:
        if line == '':
            lines_array.remove(line)
    return lines_array


def file_reader(asm_path):
    """
    reads a file, returns a list of the file's lines
    :param asm_path: the path of the .asm file to read
    :return: the array of the file's line, minus empty lines
    """
    with open(asm_path) as file:
        lines_array = file.readlines()
    lines_array = [line.strip('\n') for line in lines_array]
    return clean_empty(lines_array)


def file_writer(command_array, asm_path):
    """
    writes the array of binary commands to a new .hack file with the same name
    :param command_array: the array of binary commands
    :param asm_path: the path of the .asm file's .hack aquivilant to write to
    """
    new_name = asm_path.replace('.asm', '.hack')
    with open(new_name, "w") as file:
        for command in command_array:
            file.write(command)
            file.write('\n')


if __name__ == '__main__':
    path = "C:\\Users\\user\\Documents\\2nd\\nand2tetris\\projects\\06\\NAND-ex6\\test"
    arr = directory_parser(path)
    print("path array: ", arr)
    com_arr = ["1st binary\n", "2nd binary\n", "1010010"]
    for file_path in arr:
        print("lines from path: ", file_path, " are: ", file_reader(file_path))
        file_writer(com_arr, file_path)
        print("binary lines from path: ", file_path, " are: ", file_reader(file_path))
        print("binary lines from path: ", file_path, " are: ", file_reader(file_path))
    for item in os.listdir(path):
        if item.endswith(".hack"):
            os.remove(os.path.join(path, item))
