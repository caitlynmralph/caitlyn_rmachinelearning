import os
import csv

os.chdir("/Users/caitlynralph/Downloads/netflix-prize-data")

with open('movie_titles_cleaned.csv', 'a') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', escapechar=' ', quoting=csv.QUOTE_NONE)

    titles = open("movie_titles.csv","r").readlines()

    for i in range(0, len(titles)):
        linex = titles[i]
        index = linex.replace(',', '|', 2).find(',')
        titles[i] = titles[i][:index-1] + titles[i][index-1:].replace(',', '/')
        index0 = titles[i].find(',')
        index1 = titles[i].find(',',index0+1)
        writer.writerow([titles[i][:index0],titles[i][index0+1:index1],titles[i][index1+1:-1]])