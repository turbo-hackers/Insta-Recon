#!/usr/bin/python3
# coded by TURB0
# github https://github.com/turbo-hackers
# insta-recon v1.1

import requests
import json
import os, time

os.system("clear")
# colors
r ='\033[91m' # red
g ='\033[92m' # green
s_b ='\033[96m' # sky_blue
y ='\033[93m' # yellow
p = '\033[94m' # purple
pi = '\033[35m' # pink
reset = '\033[0m'
blink = "\033[5;96m"

def main():
	def banner():
		print(p+"""
     _____           _        _____
    |_   _|         | |      |  __ \                     
      | |  _ __  ___| |_ __ _| |__) |___  ___ ___  _ __  
      | | | '_ \/ __| __/ _` |  _  // _ \/ __/ _ \| '_ \ 
     _| |_| | | \__ \ || (_| | | \ \  __/ (_| (_) | | | |
    |_____|_| |_|___/\__\__,_|_|  \_\___|\___\___/|_| |_|
                                              """+g+"""v1.1"""+reset)
		print("           "+y+"<========[[ "+s_b+"coded by "+blink+"TURB0"+reset+y+" ]]========>\n"+reset)
		print("        "+y+"<--------( "+r+"Github : turbo-hackers"+y+" )-------->\n"+reset)
	# recon data
	def recon():
		global target, json_data, ReportList
		print(g+"┌─["+pi+"Enter Username"+g+"]"+reset)
		target = input(g+"└──>>"+y)
		print(reset)
		req = requests.Session()
		res = req.get(url="https://instagram.com/{}/?__a=1&__d=dis".format(target))
		json_data = res.json()
		ReportList = ["username","fbid","edge_followed_by","edge_follow","id","full_name","biography","is_verified","is_private","is_joined_recently","is_business_account","business_category_name","business_email","business_phone_number","hide_like_and_view_counts","profile_pic_url_hd"]
		count = 1
		print(pi+"["+y+"00"+pi+"]"+s_b+" profile link : "+g+"https://instagram.com/{}/".format(target),reset)
		for i in ReportList:
			if i == "edge_followed_by":
				print(pi+"["+y+"0{}".format(count)+pi+"]"+s_b+" {} : ".format("Followers")+g+"{}".format(json_data["graphql"]['user'][f"{i}"]["count"]))
				time.sleep(0.15)
				count +=1
			elif i == "edge_follow":
				print(pi+"["+y+"0{}".format(count)+pi+"]"+s_b+" {} : ".format("Following")+g+"{}".format(json_data["graphql"]['user'][f"{i}"]["count"]))
				time.sleep(0.15)
				count +=1
			elif count<10:
				print(pi+"["+y+"0{}".format(count)+pi+"]"+s_b+" {} : ".format(i)+g+"{}".format(json_data["graphql"]['user'][f"{i}"]))
				time.sleep(0.15)
				count +=1
			elif count>=10:
				print(pi+"["+y+"{}".format(count)+pi+"]"+s_b+" {} : ".format(i)+g+"{}".format(json_data["graphql"]['user'][f"{i}"]))
				time.sleep(0.15)
				count +=1
		print(reset)
		
	# report saving
	def save_report():
		if not os.path.exists("{}".format(target)):
			os.mkdir("{}".format(target))
		count = 1
		pic_url = json_data['graphql']['user']['profile_pic_url_hd']
		report_dict = {}
		for i in ReportList:
			if i == "edge_followed_by":
				report_dict['Followers'] = json_data["graphql"]['user'][f"{i}"]["count"]
				time.sleep(0.15)
				count +=1
			elif i == "edge_follow":
				report_dict['Following'] = json_data["graphql"]['user'][f"{i}"]["count"]
				time.sleep(0.15)
				count +=1
			elif count<10:
				report_dict['{}'.format(i)] = json_data["graphql"]['user'][f"{i}"]
				time.sleep(0.15)
				count +=1
			elif count>=10:
				report_dict['{}'.format(i)] = json_data["graphql"]['user'][f"{i}"]
				time.sleep(0.15)
				count +=1
		json_report = json.dumps(report_dict, indent=4)
		with open("{}/{}.txt".format(target,target),'w') as f:
			f.write(json_report)
			
		response = requests.get(pic_url) # download profile image
		if response.status_code:
			with open("{}/{}_profile_pic.jpg".format(target,target), 'wb') as img:
				img.write(response.content)
	# open webbrowser according to os-platform (Android/Linux/Windows)
	def open_web():
		cmd = os.popen('uname -o').readlines()
		ostype = cmd[0]
		if ostype == "Android\n" :
			os.system(f"am start -a android.intent.action.VIEW -d '{link}' > /dev/null 2>&1")
		else:
			import webbrowser
			webbrowser.open(link)

	banner()
	recon()
	print("\n")
	print(y+"[::"+s_b+"Options"+y+"::]"+reset+"\n")
	print(pi+"["+y+"1"+pi+"] -> "+s_b+"save this report"+pi+""+reset)
	print(pi+"["+y+"2"+pi+"] -> "+s_b+"open dp image in webbrowser"+reset)
	print(pi+"["+y+"0"+pi+"] -> "+s_b+"Exit"+reset+"\n")
	print(g+"┌─["+pi+"Enter option"+g+"]"+reset)
	option = int(input(g+"└──>> "+y))
	print(reset)
	if option == 1 :
		print(pi+"["+y+"Report Saving,Please wait....."+pi+"]"+reset)
		save_report()
		print("\n")
		print(g+"###"+s_b+" Report Saved Successfully "+g+"###"+reset)
	elif option == 2 :
		link = json_data['graphql']['user']['profile_pic_url_hd']
		print("\n"+pi+"[ "+g+"starting webbrowser...."+pi+" ]"+reset)
		open_web()
	elif option == 0 :
		print("\n"+pi+"["+y+"..."+pi+"]"+s_b+" Thanks for using this program...."+pi+"["+y+"..."+pi+"]"+reset+"\n")
		print(pi+"[ "+g+"Exiting...."+pi+" ]"+reset)
	else :
		print(y+"\n["+r+"Error"+y+"]"+s_b+" You are entered a wrong Input ! Please try again.")

try:
	main()
except:
	print(y+"\n["+r+"Error"+y+"]"+s_b+" Something went wrong! Please try again later!"+reset+"\n")
	print(y+"["+r+"Error"+y+"]"+s_b+""" Please Check the username you entered , 
  Check your Internet Connection ,
  If you are using VPN,
  try to turn off your vpn and try again..."""+reset+"\n")
	error_msg = input(s_b+"Press any key to Close the program ... "+reset)
	exit(0)
