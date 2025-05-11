# TODO
#
from random import randbytes

f = open("noise.wav", "wb")

# --- MASTER RIFF CHUNK START---
riff = b'\x52\x49\x46\x46'
fileSize = (0).to_bytes(4, byteorder="big") # declared further down
formatId = b'\x57\x41\x56\x45'
# --- MASTER RIFF CHUNK END ---

# --- DATA DESCRIBING CHUNK START ---
formatBlocId = b'\x66\x6d\x74\x20'
blocSize = (0x10).to_bytes(4, byteorder="little")
audioFormat = b'\x01\x00'

nbrChannels = b'\x02\x00'
frequency = (22050).to_bytes(4, byteorder="little")
bytesPerSec = (88200).to_bytes(4, byteorder="little")

bytePerBloc = b'\x04\x00'
bitsPerSample = b'\x10\x00'
# --- DATA DESCRIBING CHUNK END ---

# --- SAMPLED DATA CHUNK START ---
dataBlocID = b'\x64\x61\x74\x61'
sampledDataSize = (0).to_bytes(4, byteorder="big") # declared further down
sampledData = b'\x00'

i = 0
wait = 0
while len(sampledData) < 1048574:
    if wait % 10 == False:
        sampledData += b'\x00'
        wait += 1
        continue
    elif i == 255:
        i = 0
    else:
        sampledData += i.to_bytes(1, byteorder="big")
        i+=1

byteList = [

riff, fileSize, formatId,
formatBlocId, blocSize, audioFormat,
nbrChannels, frequency, bytesPerSec,
bytePerBloc, bitsPerSample, dataBlocID,
sampledDataSize, sampledData,

]

# count filesize
size = 0
for i in byteList:
    size += len(i)

# here lies sampledDataSize declaration
sampledDataSize = (size-44).to_bytes(4, byteorder="little")

# here lies sampledDataSize declaration
fileSize = size - 8; fileSize = fileSize.to_bytes(4, byteorder="little")
# update all changed variables in datalist
byteList[1] = fileSize
byteList[12] = sampledDataSize

# write bytes to file
for i in byteList:
    f.write(i)

f.close()
