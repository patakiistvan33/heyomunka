f = open ("gyakorlás.txt","r",encoding="utf-8")
tartalom = f.read()
f.close()
print(tartalom)


f = open ("gyakorlás.txt","r",encoding="utf-8")
adatok=[]
for sor in f:
    adatok.append(sor[:-1])
f.close()


