import requests
from bs4 import BeautifulSoup
import csv

url = requests.get("https://www.natgeotv.com/me/shows")
soup = BeautifulSoup(url.text, "lxml")
shows = soup.findAll('li', {'class': 'ListModuleItemDiv'})

with open('shows.csv', 'w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(['Show Title', 'Description'])

	for show in shows:
		title = show.find('h2', 'VMargin10').text.strip()
		description = show.find('p', 'Description').text.strip()
		writer.writerow([title, description])
		