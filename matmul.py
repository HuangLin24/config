import matplotlib.pyplot as plt
import os
FILE_PATH_LIST=sorted([name for name in os.listdir('./') if name[:3]=='log'])
Time=[[] for i in FILE_PATH_LIST]
Buffer=[[] for i in FILE_PATH_LIST]
ChunkSize=[[] for i in FILE_PATH_LIST]
Rate=[[] for i in FILE_PATH_LIST]
Rebuffer=[[] for i in FILE_PATH_LIST]
qoe=[[] for i in FILE_PATH_LIST]
bufferlist=[]
chunksizelist=[]
ratelist=[]
Rebufferlist=[]
qoelist=[]
L=['*-','x-','o-','.-','o-']


for index,filename in enumerate(FILE_PATH_LIST):
    with open(filename,'rb') as f:
        for line in f:
            par=line.split()
            Time[index].append(float(par[0]))
            Rate[index].append(float(par[1]))
            Buffer[index].append(float(par[2]))
            Rebuffer[index].append(float(par[3]))
            ChunkSize[index].append(float(par[4]))
            qoe[index].append(float(par[-1]))



for i in range(len(FILE_PATH_LIST)):
    bufferlist.append(plt.plot(Time[i],Buffer[i]))
plt.xlabel('time(s)')
plt.ylabel('buffer(s)')
plt.legend(bufferlist,labels=['node'+str(i) for i in range(len(FILE_PATH_LIST))],loc='best')
plt.title('BB buffer in mulUser env')
plt.savefig('Buffer.png')
plt.close()


for i in range(len(FILE_PATH_LIST)):
    chunksizelist.append(plt.plot(Time[i],ChunkSize[i],L[i]))
plt.xlabel('time(s)')
plt.ylabel('chunksize')
plt.legend(chunksizelist,labels=['node'+str(i) for i in range(len(FILE_PATH_LIST))],loc='best')
plt.title('BB chunksize in mulUser env')
plt.savefig('ChunkSize.png')
plt.close()

for i in range(len(FILE_PATH_LIST)):
    ratelist.append(plt.plot(Time[i],Rate[i],L[i]))
plt.xlabel('time(s)')
plt.ylabel('bitrate(kbps)')
plt.legend(ratelist,labels=['node'+str(i) for i in range(len(FILE_PATH_LIST))],loc='best')
plt.title('BB bitrate in mulUser env')
plt.savefig('Rate.png')
plt.close()

for i in range(len(FILE_PATH_LIST)):
    Rebufferlist.append(plt.plot(Time[i],Rebuffer[i],L[i]))
plt.xlabel('time(s)')
plt.ylabel('rebuffertime(s)')
plt.legend(Rebufferlist,labels=['node'+str(i) for i in range(len(FILE_PATH_LIST))],loc='best')
plt.title('BB rebuffertime in mulUser env')
plt.savefig('Rebuffer.png')
plt.close()

for i in range(len(FILE_PATH_LIST)):
    qoelist.append(plt.plot(Time[i],qoe[i],L[i]))
plt.xlabel('time(s)')
plt.ylabel('QoE')
plt.title('BB QoE in muluser env')
plt.legend(qoelist,labels=['node'+str(i) for i in range(len(FILE_PATH_LIST))],loc='best')
plt.savefig('Qoe.png')
plt.close()


