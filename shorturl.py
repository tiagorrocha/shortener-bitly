import bitly_api
import json

API_USER = "Your username from Bitly"
API_KEY = "Your key from Bitly"

b = bitly_api.Connection(API_USER, API_KEY) 
arq = open("File directory","r")
textarq = arq.read()
arq.close()
textarq = textarq.split("\n")

for line in textarq:
	arqtxt = open("namearc.txt", "a")
	res = line.replace("\r\n", "")
	short = b.shorten(uri = res) 
	for first, second in short.items():
		if ("http://bit.ly" in json.dumps(second)):
			print("Shortened url: ", json.dumps(second) )
			arqtxt.write(json.dumps(second) + "\n")
	arqtxt.close()
