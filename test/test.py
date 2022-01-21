import os
def numb():
    count = 0
    d = "templates"
    for path in os.listdir(d):
        if os.path.isfile(os.path.join(d, path)):
            count += 1
    return count