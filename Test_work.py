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
            f = open(os.path.join(path[0],i), 'r')
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
        if (i[0][-3::]!='mul') and (i[0][-3::]!='add') and (i[0]!=a):
            continue
        direct_list.append(i)
    return(direct_list)


def calc_res(dir_list):
    while(1):
        if not('mul' in dir_list[-1][1]) or not('add' in dir_list[-1][1]):
            path = dir_list[-1]
            if (path[0][-3::] != 'add') and (path[0][-3::] != 'mul'):
                for i in path[2]:           # comm1
                    if type(i) == int:
                        print("Answer is :",i)
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





