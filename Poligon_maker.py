import os
import random


def rand(start, end):
    a = random.randint(start, end)
    return (int(a))


def create_files(path, inf):
    os.chdir(path)
    num_f = rand(1, inf[4][0])
    for i in range(num_f):
        a = str(random.random()) + '.txt'
        file = open(a, 'w')
        num_numb = rand(inf[1][0], inf[1][1])
        for j in range(num_numb):
            num = rand(inf[2][0], inf[2][1])
            file.write(str(num)+' ')
        file.close()
    return(int(num_f))


def get_path_list(path):
    list_buf = []
    tree = os.walk(path)
    for i in tree:
        list_buf.append(i)
    return list_buf


def enter(inf):
    print("1. Range of amount files (a b): ")
    a, b = (input().split())
    inf[0].append(rand(int(a), int(b)))

    print("2. Range of amount numbers in each file  (a b): ")
    a, b = (input().split())
    inf[1].append(int(a))
    inf[1].append(int(b))

    print("3. Range of numbers in each file (a b): ")
    a,b = (input().split())
    inf[2].append(int(a))
    inf[2].append(int(b))

    print("4. Max dir : ")
    a = int(input())
    inf[3].append(a)

    print("5. Middle numbers of files in each dir : ")
    a = int(input())
    inf[4].append(a)






inf=[[]for i in range(5)] # [0]- rand amount files  [1]-a,b-min/max amount num in files [2]-a,b=min/max amount num in file [3]-max dir
# [4] middle num of files in dir

enter(inf)

act = ['add','mul']
path = os.getcwd()
main_path = path

for i in range(int(inf[3][0])):
    if inf[0][0] <= 0:
        print("You set a little num of files")
        input("Press any key to continue...")
        break
    main_path = os.path.join( main_path, act[rand(0,1)])
    os.makedirs(main_path)
    inf[0][0] -= create_files(main_path,inf)
    
buf = 0

while inf[0][0] > 0:
    
    if buf == inf[0][0]:
        break

    buf_list = get_path_list(path)

    for i in buf_list[1:-1]:

        if ('add' in i[1]) and ('mul' in i[1]):
            if len(i[2]) < inf[4][0]:
                inf[0][0] -= create_files(i[0], inf)
        else:
            if 'add' in i[1]:
                if rand(0, 2):
                    os.makedirs(os.path.join(i[0],'mul'))
                    inf[0][0] -= create_files(os.path.join(i[0],'mul'), inf)
                if len(i[2]) < inf[4][0]:
                    inf[0][0] -= create_files(i[0], inf)
            elif 'mul' in i[1]:
                if rand(0, 2):
                    os.makedirs(os.path.join(i[0],'add'))
                    inf[0][0] -= create_files(os.path.join(i[0],'add'), inf)
                if len(i[2]) < inf[4][0]:
                    inf[0][0] -= create_files(i[0], inf)
            else:
                if len(i[2]) < inf[4][0]:
                    inf[0][0] -= create_files(i[0], inf)























