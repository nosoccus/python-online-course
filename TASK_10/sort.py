with open("unsorted_names.txt", "r") as rf:
    names = rf.readlines()
    names.sort()
rf.close()

with open('sorted_names.txt', 'w+') as wf:
    for elem in names:
        wf.write(elem)
rf.close()
