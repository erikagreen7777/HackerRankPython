#You are given an integer, . Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)

#Different sizes of alphabet rangoli are shown below:

#size 3

#----c----
#--c-b-c--
#c-b-a-b-c
#--c-b-c--
#----c----

#size 5

#--------e--------
#------e-d-e------
#----e-d-c-d-e----
#--e-d-c-b-c-d-e--
#e-d-c-b-a-b-c-d-e
#--e-d-c-b-c-d-e--
#----e-d-c-d-e----
#------e-d-e------
#--------e--------

#size 10

#------------------j------------------
#----------------j-i-j----------------
#--------------j-i-h-i-j--------------
#------------j-i-h-g-h-i-j------------
#----------j-i-h-g-f-g-h-i-j----------
#--------j-i-h-g-f-e-f-g-h-i-j--------
#------j-i-h-g-f-e-d-e-f-g-h-i-j------
#----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
#--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
#j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
#--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
#----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
#------j-i-h-g-f-e-d-e-f-g-h-i-j------
#--------j-i-h-g-f-e-f-g-h-i-j--------
#----------j-i-h-g-f-g-h-i-j----------
#------------j-i-h-g-h-i-j------------
#--------------j-i-h-i-j--------------
#----------------j-i-j----------------
#------------------j------------------
#The center of the rangoli has the first alphabet letter a, and the boundary has the  alphabet letter (in alphabetical order).

#Function Description

#Complete the rangoli function in the editor below.

#rangoli has the following parameters:

#int size: the size of the rangoli
#Returns

#string: a single string made up of each of the lines of the rangoli separated by a newline character (\n)
#Input Format

#Only one line of input containing , the size of the rangoli.

#Constraints
#0 < size < 27

# NOTE: created using Python3

def print_rangoli(size):
    try:
        size > 0 and size < 27
    except:
        print("error: please enter a number greater than 0 and less than 27")
    else:
        alphList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        dimensionLetterCount = (size * 2) - 1
        widestDashCount = (size - 1) * 2
        totalRangoliWidth = dimensionLetterCount + widestDashCount
        ymidlineLetterIncrementer = size-1
        for i in range(dimensionLetterCount):
            yMidline = dimensionLetterCount - 1
            xMidline = dimensionLetterCount
            xmidlineLetterIncrementer = 1
            leftLetterCountFromMidline = xMidline - size - ymidlineLetterIncrementer
            currentRowValues = []

            for j in range(totalRangoliWidth + 1):
                currentRowValuesCount = len(currentRowValues)
                if ( j == yMidline):
                    print(alphList[ymidlineLetterIncrementer], end="")
                    currentRowValues.append(alphList[ymidlineLetterIncrementer])
                elif (j % 2 == 0 and j < xMidline and j == yMidline - (leftLetterCountFromMidline * 2)):    
                    print(alphList[size - xmidlineLetterIncrementer], end="")
                    currentRowValues.append(alphList[size - xmidlineLetterIncrementer])
                    xmidlineLetterIncrementer +=1
                    leftLetterCountFromMidline -= 1
                elif (j == xMidline):
                    xmidlineLetterIncrementer -=1
                    leftLetterCountFromMidline = xMidline - size - ymidlineLetterIncrementer
                elif (j % 2 != 0 and j > xMidline and (currentRowValuesCount - int((j-xMidline)/2) > 0)):
                    print(currentRowValues[currentRowValuesCount - int((j-xMidline)/2) - 1], end="")
                    xmidlineLetterIncrementer -=1
                    leftLetterCountFromMidline -= 1
                else:
                    print("-", end="")
            
            print()
            if (i < size-1):
                ymidlineLetterIncrementer -= 1
            elif (i >= size-1):
                ymidlineLetterIncrementer += 1
               
if __name__ == '__main__':
