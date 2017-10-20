file=open('running-config.cfg','r')
file1=open('confignewip.cfg','w')
#for replace ip address
for line in file:
	file1.write(line.replace('172','192'))
	
file1.close()
