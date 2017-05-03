from struct import *
import time
timetaken = time.time()
readfile = open("C:/Users/Dhruv/Desktop/LZW/large.txt", "r")
content = readfile.read()
length = len(content)
readfile.close()

codes=[chr(i) for i in range(256)]
    
writefile = open("C:/Users/Dhruv/Desktop/LZW/compressed_read.bin", "wb")
current_string = ""
ans = ""
for i in range(0, length) :
    temp = current_string + content[i]
    if temp in codes :
        current_string += content[i]
    else :
        codes.append(current_string + content[i])
        binary = pack('h', codes.index(current_string))
        ans += codes[codes.index(current_string)]
        writefile.write(binary)
        current_string = content[i]
        
writefile.write(pack('h', codes.index(current_string)))
ans += codes[codes.index(current_string)]
writefile.close()
timetaken = time.time() - timetaken
print(timetaken)