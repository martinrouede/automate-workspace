#!/usr/bin/python3
import os
import sys
import platform
import json

def main():
	path = os.path.dirname(os.path.abspath(__file__))
	f = open(path+'/commands.json')
	commands = json.load(f)

	if(len(sys.argv) != 2 or int(sys.argv[1]) < 0 or int(sys.argv[1]) >= len(commands)):
		print("Se espera recibir como argumento el indice del comando que quiera ejecutar")
		sys.exit()

	command = commands[int(sys.argv[1])]
	
	os.chdir(command["path"])
	os.system("code .")

	if(platform.system() == "Linux"):
		os.system("gnome-terminal --tab --title='"+command["path"]+"'")
	if(platform.system() == "Windows"):
		os.system("start cmd /k powershell")
	

	for s in command["scripts"]:
		if(platform.system() == "Linux"):
			os.system("gnome-terminal --tab --title='"+s+"' -- "+s+"")
		if(platform.system() == "Windows"):
			os.system("start cmd /k "+s+"")

main()