import csv

def prb(c,a,b,n):
    with open('train_data.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)    	
        count=0
        for row in csv_reader:
            if(row[c]==a and row[n]==b):
                count+=1
    return(count)

def clas(b,n):
    with open('train_data.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)    	
        count=0
        for row in csv_reader:
            if row[n]==b:
                count+=1
    return count


def no():
    with open('train_data.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)    	
        s=[]
        firstline=1
        for row in csv_reader:
            if firstline==1:
                firstline=0
            elif(row[4] not in s):
                s.append(row[4])
        return(s)


total=0
cols=-1
with open('train_data.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        total+=1
    cols=len(row)-1


arr=no()
classes=len(arr)

prbclass=[0 for i in range(classes)]
for i in range(classes):
    prbclass[i]=clas(arr[i],cols)
    
#t is matrix which stores probablity with respect to class
t= [ [ 0 for i in range(classes) ] for j in range(cols) ]
for i in range(cols):
    print("Enter column",end=" ")
    print(i)
    ans=input()
    for j in range (classes):
        t[i][j]=(prb(i,ans,arr[j],cols)/prbclass[j])
        

finalprb=[0 for i in range(classes)]
for j in range(classes):
    mul=1
    for i in range(cols):
        mul=mul*t[i][j]
    finalprb[j]=mul*(prbclass[j]/total)

print("Maximum Probablity is of class = ",end=" ")
print(arr[finalprb.index(max(finalprb))])
