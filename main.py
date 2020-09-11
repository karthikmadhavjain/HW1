#Author: Karthik Madhav Jain kmj5614@psu.edu
global gradepoint
inputnumber= 0
def getGradePoint ():
  global gp1,gp2,gp3
  
  
  if inputnumber == 1:
    grade = c1
  if inputnumber == 2:
    grade = c2
  if inputnumber == 3:
    grade = c3
  if grade == 'A':
    gradepoint = 4.0
  elif grade == 'A-':
    gradepoint = 3.67
  elif grade == 'B+':
    gradepoint = 3.33
  elif grade == 'B':
    gradepoint = 3.0
  elif grade == 'B-':
    gradepoint = 2.67
  elif grade == 'C+':
    gradepoint = 2.33
  elif grade == 'C':
    gradepoint = 2.0
  elif grade == 'D':
    gradepoint = 1.0
  else: gradepoint = 0.0

  if inputnumber == 1:
    gp1=gradepoint
  if inputnumber == 2:
    gp2=gradepoint
  if inputnumber == 3:
    gp3=gradepoint

  
  print('Grade point for course %s is:'%inputnumber,gradepoint)


c1 = str (input('Enter your course 1 letter grade: '))
cc1 = int (input('Enter your course 1 credit: '))
inputnumber = inputnumber+1
getGradePoint()

c2 = str (input('Enter your course 2 letter grade: '))
cc2 = int (input('Enter your course 2 credit: '))
inputnumber = inputnumber+1
getGradePoint()

c3 = str (input('Enter your course 3 letter grade: '))
cc3 = int (input('Enter your course 3 credit: '))
inputnumber = inputnumber+1
getGradePoint()

credittotal = cc1+cc2+cc3
gpa = ((cc1*gp1)+(cc2*gp2)+(cc3*gp3))/credittotal

print('Your GPA is:',gpa)
