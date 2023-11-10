##myFile = open("sample.txt")
##line = myFile.readline()
##while line:
##    print(f"{line!r}")
##    line = myFile.readline()
##print(f"{line!r}")
##myFile.close()

out_file = open("output.txt", "w")
out_file.write("\nCountdown has begun\n")
for i in range(4, 0, -1):
    out_file.write(f"\t\t{i}...\n")
out_file.write("Blastoff!")
out_file.close()
