x,y = [int(x) for x in (input()).split(" ")]

queue = [int(x) for x in (input()).split(" ")]

for i in range(y):
    l = len(queue)
    if l <= y:
        temp_queue = queue
    else:
