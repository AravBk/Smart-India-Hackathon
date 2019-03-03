import csv
import plotly as py
import plotly.graph_objs as go
from datetime import datetime

moviefile = open("movies.csv","r")
mv = csv.reader(moviefile)
next(mv,None)

userfile = open("users.csv","r")
us=csv.reader(userfile)
next(us,None)

countmovies= len(list(mv))
countusers= len(list(us))
moviefile.seek(0)
userfile.seek(0)

def Cloning(li1): 
    li_copy = list(li1) 
    return li_copy

moviefile.seek(0)
gencount = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
genre = ['Biography','Horror','Crime','Animation','Musical','Romance','Family','Comedy','Thriller','Mystery','History','Sci-Fi','Fantasy','Drama','Sport','War']
listd = []
for row in mv:    
    listd = (row[8])
    for j in range(0,16):
        if listd.find(genre[j])!=-1:
            gencount[j]+=1

trace = go.Pie(labels=genre, values=gencount)
py.offline.plot([trace], filename='genre_splitup.html',auto_open=False)
print("Generated Genre Splitup")