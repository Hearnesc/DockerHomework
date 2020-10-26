import glob, os, socket
max = 0
maxname = ""
total = 0
dir = "/home/data/"
out = "/home/output/"
f = open(out + "result.txt", "w")
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
os.chdir(dir)
for filename in glob.glob("*.txt"):
    file = open(dir+filename, "r")
    data = file.read()
    words = data.split()
    if len(words) >= max:
        max = len(words)
        maxname = filename
    f.write(filename + ": Words: " + str(len(words)) + "\n")
    total += len(words)
    file.close()
f.write("\nTotal words: " + str(total) + "\nMaximum words file: " + maxname + ": Words: " + str(max) +"\nIP Address: " + ip + "\n\n")
f.close()
final = open(out + "result.txt", "r")
print(final.read())
final.close()
