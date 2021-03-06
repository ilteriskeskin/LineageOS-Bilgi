import os
import yaml

print("Dosyaların güncelliği kontrol ediliyor...")
os.system("git pull https://github.com/LineageOS/lineage_wiki.git")

print("Telefonların listesini barındıran dosya oluşturuluyor...")
os.system("ls lineage_wiki/_data/devices/ > lineage_wiki/_data/devices/output.txt")

print("LineageOS Destekleyen Telefonlar: ")

file_names = []

f = open("lineage_wiki/_data/devices/output.txt", "r")

for i in f:
    a = f.readline()
    print(i,a)
    file_names.append(a)

f.close()

for i in range(len(file_names)-1):
    file_path = "/home/ilteriskeskin/Belgeler/LineageOS-Bilgi/lineage_wiki/_data/devices/" + file_names[i].rstrip()
    with open(file_path, "r") as stream:
        try:
            file = yaml.load(stream, Loader=yaml.FullLoader)
            print(i + 1,file["vendor"], file["name"])
        except:
            print()

phone1 = int(input("RAM miktarlarını karşılaştırmak istediğin 1. telefonun numarasını gir: "))
phone2 = int(input("RAM miktarlarını karşılaştırmak istediğin 2. telefonun numarasını gir: "))

phone1_path = "/home/ilteriskeskin/Belgeler/LineageOS-Bilgi/lineage_wiki/_data/devices/" + file_names[phone1 - 1].rstrip()
phone2_path = "/home/ilteriskeskin/Belgeler/LineageOS-Bilgi/lineage_wiki/_data/devices/" + file_names[phone2 - 1].rstrip()

with open(phone1_path, "r") as stream1:
    try:
        file1 = yaml.load(stream1, Loader=yaml.FullLoader)
        ram1 = file1["ram"]
    except:
        print()

with open(phone2_path, "r") as stream2:
    try:
        file2 = yaml.load(stream2, Loader=yaml.FullLoader)
        ram2 = file2["ram"]
    except:
        print()


if int(ram1[0]) > int(ram2[0]):
    print("{}'in RAM miktari {}'dan fazla".format(phone1, phone2))
elif int(ram2[0]) > int(ram1[0]):
    print("{}'in RAM miktari {}'dan fazla".format(phone2, phone1))
else:
    print("Modellerin RAM miktarları eşit.")
