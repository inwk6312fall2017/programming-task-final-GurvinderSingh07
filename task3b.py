file=open('running-config.cfg','r')
file2=open('confignewaccess.cfg','w')
#for replace ip address
for line in file:
	if 'access-list' in line:
		file2.write(line)

file2.close()


