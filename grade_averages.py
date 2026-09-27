import grades

my_2file = open("grades_avg.csv")

for line in my_2file:
    print(len(line))
    print(line.strip())

my_2file.close()



