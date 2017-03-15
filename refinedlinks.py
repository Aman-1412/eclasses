import re,sys
with open(sys.argv[1],"r") as f:
	x = re.findall('http.*',f.read())
print x
with open("ready.txt","w") as f:
	f.write("\n".join(x))