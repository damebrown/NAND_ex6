import file_parser as fp
import first_pass as first
import second_pass as second
import sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('No folder was specified. please enter a file or folder'
              'name in system args.')
    else:
        for i in range(1, len(sys.argv)):
            file_list = fp.directory_parser(sys.argv[i])
            for path in file_list:
                try:
                    lines = fp.file_reader(path)
                    clean_code, symbol_table = first.first_pass(lines)
                    assembled_code = second.second_pass(clean_code,
                                                        symbol_table)
                    fp.file_writer(assembled_code, path)
                except SyntaxError as e:
                    print("Error assembling file:\n{0}"
                          "\nwith Error:\n{1}".format(path, e.msg))
