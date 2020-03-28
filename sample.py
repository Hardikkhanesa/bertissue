#from . import sanlpbert
from sanlpbert import BertAnalyzer
#related
from datetime import datetime

b = BertAnalyzer()

list1 = ["South Korea’s ruling political party announces a Green New Deal manifesto to be included in legislation, including discontinuation of coal project financing and introduction of a carbon tax. Go climate lea",]
aaa = "South Korea’s ruling political party announces a Green New Deal manifesto to be included in legislation, including discontinuation of coal project financing and introduction of a carbon tax. Go climate lea"
bbb = "politics"

mylist = []
'''
for i in range(10):

    mylist.append(b.getRelavance(aaa,bbb))

print(mylist)
'''


currenttime = datetime.now()

myaspect=[]
for i in range(100):
    mylist.append("South Korea’s ruling political party announces a Green New Deal manifesto to be included in legislation, including discontinuation of coal project financing and introduction of a carbon tax. Go climate lea")
    myaspect.append("politics")

b.getRelavance(mylist,myaspect)
print("testing took time ", datetime.now() - currenttime)
#print(b.getRelavance(mylist,myaspect))


'''
for i in range(5):

    e = b.getRelavance("South Korea’s ruling political party announces a Green New Deal manifesto to be included in legislation, including discontinuation of coal project financing and introduction of a carbon tax. Go climate lea","politics")
    print(e)

a =b.getRelavance("All Indian airlines will report significant losses in 1st quarter of this year and may initially ground around 150 planes as shock from #coronavirus pandemic","movies")
print(a)


bi = b.getRelavance("That movie was absolutely awful","movie")
print(bi)

#movie related
c= b.getRelavance("That movie was absolutely awful","sports")
print(c)

#aviation related
d= b.getRelavance("All Indian airlines will report significant losses in 1st quarter of this year and may initially ground around 150 planes as shock from #coronavirus pandemic","aviation")
print(d)


'''