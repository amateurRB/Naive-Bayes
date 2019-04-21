import pandas as pd

data=pd.read_csv("rating.csv")
table=data["table"].values
rating=data["rating"].values
votes=data["votes"].values
output=data["output"].values
y,n=0,0


for i in output:
    if i==1:
        y=y+1
    else:
        n=n+1
print(y,n)



pYes= y/data.shape[0]   #later multiply thissss
pNo= n/data.shape[0]

print(pYes)
print(pNo)

#has booking


ytable,ntable=0,0
#pytable,pntable=0,0

t=int(input("enter table booking. 1=Present; 2=Absent"))
r=int(input("enter rating. 1,2,3,4"))
#v=input("enter votes")


for k,j in zip(table,output):
    if k==t:
        if j==1:
            ytable= ytable+1
        else:
            ntable= ntable+1
pytable= ytable/y
nytable=ntable/n
print(pytable)
print(nytable)

#Rating
yr,nr=0,0

for l,m in zip(rating,output):
    if l==r:
        if m==1:
            yr= yr+1
        else:
            nr= nr+1
pyrating= yr/y
nyrating=nr/n
print("yes rating",pyrating)
print("no rating",nyrating)


pyesss=pytable*pyrating*pYes
pnooo=nyrating*nytable*pNo
print(pyesss)
print(pnooo)
#print(pytable)
            
        