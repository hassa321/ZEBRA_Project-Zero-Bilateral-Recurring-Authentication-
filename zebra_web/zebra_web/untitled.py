def map_sequences(keypresses,keyreleases,watch_data):
    #Assuming keypress and keyreleases in form of [ [timestamp, key], [timestamp, key]... ] 
    #Assuming watch_data is a list of lists [ [ x, y, z, timestamp]......  ]

    sequences = []
    predictions = []

   

    for i in range(len(keys_pressed)):

    start = int(keys_released[i][0])
    end = int(keys_pressed[i][0])

    sequence = []

    while len(copy_acc) != 0:
    # We want to remove the line so we dont have to iterate trough everything again
    line = copy_acc.pop(0)
    if line == ['']:
      continue 

    time, acc_x, acc_y, acc_z = line[0], line[1], line[2], line[3]

    current_time = int(time)

    if current_time < start:
      continue 
    if current_time >= end:
      break 

    sequence.append([float(acc_x), float(acc_y), float(acc_z)])
    predictions.append(key)
    sequences.append(sequence)