file_name = 'mbox-short.txt'

file = open(file_name, mode ='a')
movie_name = ['Wow','far','free', 'Diary']

for movie in movie_name:
    file.write(movie)
    file.write('\n')
    print(file)