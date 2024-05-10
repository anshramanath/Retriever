from bs4 import BeautifulSoup
import requests 
import csv

pg = requests.get("https://www.utrecsports.org/intramurals/todays-games")
soup = BeautifulSoup(pg.text, "html.parser")

i = 0
blackTeam = []
whiteTeam = []
for team in soup.findAll("td", attrs = {"style":"color:black !important;"}):
    if i % 2 == 0:
        blackTeam += [team]
    else:
        whiteTeam += [team]
    
    i += 1

whereabouts = soup.findAll("td", attrs = {"rowspan":"2"})

file = open("GamesToday2.csv", "w")
writer = csv.writer(file)
writer.writerow(["Team White", "Team Black", "Place & Time"])

for team1, team2, whereabout in zip(blackTeam, whiteTeam, whereabouts):
    writer.writerow([team1.text, team2.text, whereabout.text])

file.close()

