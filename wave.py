f = open("noise.wav", "wb")

riff = b'\x52\x49\x46\x46' #1
# fileSize (declared further down) #2
formatId = b'\x57\x41\x56\x45' #3

byteList = [

riff, b'\x00\x00\x00\x00', formatId,



]

# count filesize
size = 0
for i in byteList:
    size += len(i)

# turn filesize to little endian bytes
fileSize = size - 4; fileSize = fileSize.to_bytes(4, byteorder="little")
print(fileSize)
# change filesize 
byteList[1] = fileSize
print(byteList[1])

# write bytes to file
for i in byteList:
    f.write(i)

f.close()