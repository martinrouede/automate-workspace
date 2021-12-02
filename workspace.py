#!/usr/bin/python3
import os
import sys

commands = [
	{
		"path": "Documents/Porthos/Artear-PageBuilder-Fusion-Features/",
		"scripts": ["npm run dev", "npx fusion start"]
	},
	{
		"path": "Documents/Porthos/artear-outboundfeeds/",
		"scripts": ["npx fusion start"]
	},
	{
		"path": "Documents/Porthos/tn-elections-widget/",
		"scripts": ["npm run start"]
	}
]

def main():
	if(len(sys.argv) != 2 or int(sys.argv[1]) < 0 or int(sys.argv[1]) >= len(commands)):
		print("Se espera recibir como argumento el indice del comando que quiera ejecutar")
		sys.exit()

	command = commands[int(sys.argv[1])]
	os.chdir(command["path"])
	os.system("gnome-terminal --tab --title='"+command["path"]+"'")

	for s in command["scripts"]:
		os.system("gnome-terminal --tab --title='"+s+"' -- "+s+"")

main()