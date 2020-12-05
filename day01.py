inputFile = open('data/day01.txt', "r")

years = inputFile.readlines()
years = list(map(lambda x: int(x.replace('\n', '')), years))

for i in range(len(years)):
    for k in range(i, len(years)):
        if years[i] + years[k] == 2020:
            print('Teil 1:')
            print(years[i] * years[k])
        for j in range(k, len(years)):
            if years[i] + years[k] + years[j] == 2020:
                print('Teil 2:')
                print(years[i] * years[k] * years[j])
