print ("TIMES TABLES")
times_table = 12
for i in range(1, times_table + 1):
    for j in range(0, times_table + 1):
        answer = i * j

        print(f"{j} x {i} = {answer}")
