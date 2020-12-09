# Assignment_1
# Question no.1
name=input("Enter Name....")
def foo():
    for i in range(len(name)):
        for j in range(len(name)):
            if i == j:
                print(name[i], end="")
            else:
                print(' ', end="")
        print()
foo()
name1=input("Enter Name....")
def foo1():
    for i in range(len(name1)+1):
        for j in range(len(name1),0,-1):
            if i == j:
                print(name1[len(name1)-j], end="")
            else:
                print(' ', end="")
        print()
foo1()


##Takes an input and prints it diagonally and takes an other input to print on reverse digonal
##Output is given below

Enter Name....Asma
A   
 s  
  m 
   a
Enter Name....Asma
    
   a
  m 
 s  
A   

## Question No.02
def Stu():
    roll_num=int(input("Enter roll number.."))
    Name=input("Enter Student Name...")
    Age=int(input("Enter Student Age..."))
    Marks=int(input("Enter Student Marks"))
    if(Marks>100):
        Marks=int(input("Enter Student Marks"))
    l=[roll_num,Name,Age,Marks]
    return l

average=[]
def highest_Stu(l1,l2):
    if(l1[3]<l2[3]):
        highest=l2[3]
    elif(l1[3]>l2[3]):
        highest=l1[3]
    return highest
def lowest_Stu(l1,l2):
    if(l1[3]<l2[3]):
        lowest=l1[3]
    elif(l1[3]>l2[3]):
        lowest=l2[3]
    return lowest

def average_Stu(l1):
    average.append(l1[3])
    return average


print (" For Student 1")
l1=Stu()
highest=l1[3]
lowest=l1[3]
average=average_Stu(l1)
print (" For Student 2")
l2=Stu()
highest=highest_Stu(l1,l2)
lowest=lowest_Stu(l1,l2)
average=average_Stu(l2)
print (" For Student 3")
l3=Stu() 
highest=highest_Stu(l2,l3)
lowest=lowest_Stu(l2,l3)
average=average_Stu(l3)
print (" For Student 4")
l4=Stu()
highest=highest_Stu(l3,l4)
lowest=lowest_Stu(l3,l4)
average=average_Stu(l4)
print (" For Student 5")
l5=Stu()  
highest=highest_Stu(l4,l5)
lowest=lowest_Stu(l4,l5)
average=average_Stu(l5)
l={"Student 1":l1,
  "Student 2":l2,
  "Student 3":l3,
  "Student 4":l4,
  "Student 5":l5
  }
print("Student 1:  ",l.get("Student 1","Does not Exist"))
print("Student 2:  ",l.get("Student 2","Does not Exist"))
print("Student 3:  ",l.get("Student 3","Does not Exist"))
print("Student 4:  ",l.get("Student 4","Does not Exist"))
print("Student 5:  ",l.get("Student 5","Does not Exist"))
sum=0
for i in range(len(average)):
    sum=sum+int(average[i])
    
sum=float(sum/len(average))
    
print("Class Highest:  ",highest)
print("Class Lowest;   ",lowest)
print("Class Average:   ",sum)

## Take 5 inputs of 5 students with roll number age name and marks store them in indiviusal list and then store those list to the dictionaries
## calculate highest , lowest and averrage among those five and print it
## output is given below

  For Student 1
Enter roll number..2356
Enter Student Name...Asma
Enter Student Age...34
Enter Student Marks56
 For Student 2
Enter roll number..7990
Enter Student Name...Talha
Enter Student Age...23
Enter Student Marks78
 For Student 3
Enter roll number..7787
Enter Student Name...Qasim
Enter Student Age...34
Enter Student Marks90
 For Student 4
Enter roll number..4535
Enter Student Name...haris
Enter Student Age...32
Enter Student Marks67
 For Student 5
Enter roll number..6798
Enter Student Name...Aliya
Enter Student Age...46
Enter Student Marks78
Student 1:   [2356, 'Asma', 34, 56]
Student 2:   [7990, 'Talha', 23, 78]
Student 3:   [7787, 'Qasim', 34, 90]
Student 4:   [4535, 'haris', 32, 67]
Student 5:   [6798, 'Aliya', 46, 78]
Class Highest:   78
Class Lowest;    67
Class Average:    73.8

## Question No.3

import time
###from random import randint
song="""Why is everyone so down?,
What's the problem; say something,
It’s so icy here,
Is this the trend these days?,
Why is everyone so boring?,
Actually; I guess I'm the same,
Tell me what I got to do,
Hurry and turn on the bluetooth,

[Chorus],
Just put any song on,
Anything fun,
Just dance however you want,
As if you're just fine,
Don’t wanna think about anything,
I just wanna live for a moment,
I'm sick and tired of my everyday,
Keep it up; one more song,

[Verse 1],
Just put any song on,
Who cares; it's so boring,
I think we need to refresh,
From our built up stress,
I wanna laugh till my belly button falls off today,
What up my dawgs; where are you,
Come over with some beer and chips; huh,
"""
print("Actual Song:  \n",song)
t=0.55
x=song.split(",")
print("Song After Splitting:   ")
for i in range(len(x)):
    print(x[i],"\n")
   ## t=randint(0.5,1)
    time.sleep(t)
   
##Takes a song an use split funtion to store it in a list and then print very line of list after every 0.5 seconds
##Output is given below

Actual Song:  
 Why is everyone so down?,
What's the problem; say something,
It’s so icy here,
Is this the trend these days?,
Why is everyone so boring?,
Actually; I guess I'm the same,
Tell me what I got to do,
Hurry and turn on the bluetooth,

[Chorus],
Just put any song on,
Anything fun,
Just dance however you want,
As if you're just fine,
Don’t wanna think about anything,
I just wanna live for a moment,
I'm sick and tired of my everyday,
Keep it up; one more song,

[Verse 1],
Just put any song on,
Who cares; it's so boring,
I think we need to refresh,
From our built up stress,
I wanna laugh till my belly button falls off today,
What up my dawgs; where are you,
Come over with some beer and chips; huh,

Song After Splitting:   
Why is everyone so down? 


What's the problem; say something 


It’s so icy here 


Is this the trend these days? 


Why is everyone so boring? 


Actually; I guess I'm the same 


Tell me what I got to do 


Hurry and turn on the bluetooth 



[Chorus] 


Just put any song on 


Anything fun 


Just dance however you want 


As if you're just fine 


Don’t wanna think about anything 


I just wanna live for a moment 


I'm sick and tired of my everyday 


Keep it up; one more song 



[Verse 1] 


Just put any song on 


Who cares; it's so boring 


I think we need to refresh 


From our built up stress 


I wanna laugh till my belly button falls off today 


What up my dawgs; where are you 


Come over with some beer and chips; huh 


