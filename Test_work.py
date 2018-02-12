import os


def calc_files(path):  # calculate result in one dir
    list_file = []
    act = path[0][-3::]
    if act == 'add':
        buf = 0
    else:
        buf = 1
    for i in path[2]:
        if type(i) == str:

            if i[-2::] == 'py':
                continue

            f = open(path[0]+'\\'+i, 'r')
            list_file += f.read().split()
        else:
            list_file.append(i)

    for i in list_file:
        if act == 'add':
            buf += int(i)
        else:
            buf *= int(i)
    return (buf)


def get_dir_list(dir):   # get list of directory
    direct_list = []
    direct_buf = os.walk(dir)
    for i in direct_buf:
        direct_list.append(i)
    return(direct_list)


def calc_res(dir_list):
    while(1):
        if not(dir_list[-1][1]):
            path = dir_list[-1]
            if (path[0][-3::] != 'add') and (path[0][-3::] != 'mul'):
                print("Answer is :",path[2][-1])
                return()
            buf = calc_files(path)
            for i in dir_list:
                if i[0] == path[0][0:-4]:

                    i[1].remove(path[0][-3::])
                    i[2].append(buf)

            del dir_list[-1]


dir_list = get_dir_list(os.getcwd())
calc_res(dir_list)

input("Press any key...")





