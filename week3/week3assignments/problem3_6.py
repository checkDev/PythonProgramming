import sys
#def calLen(infile, outfile):

infile = open(sys.argv[1])
outfile = open (sys.argv[2] ,'w')
for line in infile:
    line = line.strip("\n")
    outfile.write(str(len(line))+"\n")
infile.close()
outfile.close()
