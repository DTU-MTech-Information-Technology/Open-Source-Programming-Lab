num_list = [1, 7, -9, 21, 11, 0, -22, 5, -4, -1, 8]

i = 2 # third one
size = len(num_list)
while True:
    print(num_list.pop(i))
    
    size -= 1
    if size <= 0:
        break
    
    i = (i+2)%size
