import time
timetaken = time.time()
decompress = open("C:/Users/Dhruv/Desktop/LZW/write.bin", "rb")
content = decompress.read()
decompress.close()

codes = []
for i in range(0, 256) :
    codes.append(chr(i))

val = content[0] + content[1] + (content[1])*255
ans = codes[val]
old = codes[val]
for i in range(3, len(content), 2):
    val = content[i-1] + content[i] + (content[i])*255
    if(val < len(codes)):
        ans += codes[val]
        codes.append(old + codes[val][0])
        old = codes[val]
    else:
        codes.append(old + old[0])
        ans += (old + old[0])
    old = codes[val]

outcome = open("C:/Users/Dhruv/Desktop/LZW/decompressed_read.txt", "w")
outcome.write(ans)
outcome.close()
timetaken = time.time() - timetaken
print(timetaken)