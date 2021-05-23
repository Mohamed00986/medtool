import sys,os,time,pyshorteners

os.system("clear")

def jalan(z):
	for e in z + '\n' :
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.10)
		




print("\033[1;31m                    This Tool By DARK BOY (li 7wak)")
time.sleep(3)

os.system("clear")
logo = """

██████╗░░█████╗░██████╗░██╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
██║░░██║███████║██████╔╝█████═╝░
██║░░██║██╔══██║██╔══██╗██╔═██╗░
██████╔╝██║░░██║██║░░██║██║░╚██╗
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝

██████╗░░█████╗░██╗░░░██╗  ██╗░░░░░██╗
██╔══██╗██╔══██╗╚██╗░██╔╝  ██║░░░░░██║
██████╦╝██║░░██║░╚████╔╝░  ██║░░░░░██║
██╔══██╗██║░░██║░░╚██╔╝░░  ██║░░░░░██║
██████╦╝╚█████╔╝░░░██║░░░  ███████╗██║
╚═════╝░░╚════╝░░░░╚═╝░░░  ╚══════╝╚═╝

███████╗░██╗░░░░░░░██╗░█████╗░██╗░░██╗
╚════██║░██║░░██╗░░██║██╔══██╗██║░██╔╝
░░░░██╔╝░╚██╗████╗██╔╝███████║█████═╝░
░░░██╔╝░░░████╔═████║░██╔══██║██╔═██╗░
░░██╔╝░░░░╚██╔╝░╚██╔╝░██║░░██║██║░╚██╗
░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚═╝"""

print (logo)
print("")
print("")
print("\033[1;32m")

def list():
	print ("                    [1] hadi ba9i ma9aditha")
	print ("                    [2] Shorter Link")
	print ("                    [3] My Channel youtube ")
	print ("                    [4] My WhatsApp ")
	print ("                    [5] My Instagram")
	
	print ("\033[1;31m                    [0] Exit")

list()
print ("")

khtar =  input ("\033[1;36m        [?]   Choose : ")

if khtar == "1":
	os.system("clear")
	print ("\033[1;31mError 404")
	print ("\033[1;31mError 404")
	print ("\033[1;31mError 404")
	print ("\033[1;31mError 404")
	print ("\033[1;31mError 404")
	print ("\033[1;31m                    Error 408")
	print ("\033[1;31m                    Error 408")
	print ("\033[1;31m                    Error 408")
	print ("\033[1;31m                    Error 408")
	print ("\033[1;31m                    Error 408")
	print ("\033[1;31m                    Error 408")
	print ("\033[1;31m                                        Error 501")
	print ("\033[1;31m                                        Error 501")
	print ("\033[1;31m                                        Error 501")
	print ("\033[1;31m                                        Error 501")
	print ("\033[1;31m                                        Error 501")
	print ("\033[1;31m                                        Error 501")
	print ("")
	print("")
	jalan ("\033[1;34m     SIR T9AWED RAH BA9I MA9ADIT HAD LBLASA :/ ")
	time.sleep(2)
	os.system("python3 tool.py")



    
elif khtar == "2":
	os.system("clear")
	print ("                     This tool need a internet ")
	print("")
	print("")
	url = input ("\033[1;33m          Enter your URL :\033[1;31m ")
	print("")
	s = pyshorteners.Shortener().tinyurl.short(url)
	print('')
	jalan ("\033[1;34m       Your Url Shorted ===>  "+ s)
	
	def ex():
		print("")
		print("")
		print ("\033[1;34m                         [1] Back to tool")
		print("")
		print ("\033[1;34m                         [0] Exit ")
		print("")
		ex = input ("\033[1;35m                    [?] choose : ")
		if ex == "1":
			os.system("python3 tool.py")
		elif ex == "0":
			print ("")
			print("")
			jalan ("\033[1;32m                     GOOD BYE BOSS")
				
	ex()

			
		


	
	




elif khtar == "0":
	print ("\033[1;34m                      Good Bye")
	


elif khtar == "3":
	print("")
	print("")
	jalan ("\033[1;33m       Welcome To My Channel Please Subscribe ")
	time.sleep(3)
	os.system(' xdg-open https://youtube.com/channel/UChvm8repsoRnHeWUT5zXOvQ')
	os.system("python3 tool.py")	
elif khtar == "4":
	print("")
	print("")
	jalan ("\033[1;34m              Welcome To My comte WhatsApp  ")
	time.sleep(5)
	os.system(' xdg-open https://api.whatsapp.com/send/?phone=212697073632&text&app_absent=0')
	os.system("python3 tool.py")
	
elif khtar == "5":
	print("")
	print("")
	jalan ("\033[1;30m             Welcome To My instagram ")
	time.sleep(3)
	os.system(' xdg-open https://www.instagram.com/blackx_mohamed?r=nametag')
	os.system("python3 tool.py")


else:
	jalan ("\033[1;31m  3awd ktb lcode rah machi howa ktb 1 oula 2 oula 3 oula 4 oula 0")
	time.sleep(4)
	os.system("python3 tool.py")
	