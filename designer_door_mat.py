# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

# Mat size must be X. ( is an odd natural number, and  is  times .)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.
# Sample Designs

#     Size: 7 x 21 
#     ---------.|.---------
#     ------.|..|..|.------
#     ---.|..|..|..|..|.---
#     -------WELCOME-------
#     ---.|..|..|..|..|.---
#     ------.|..|..|.------
#     ---------.|.---------
    
#     Size: 11 x 33
#     ---------------.|.---------------
#     ------------.|..|..|.------------
#     ---------.|..|..|..|..|.---------
#     ------.|..|..|..|..|..|..|.------
#     ---.|..|..|..|..|..|..|..|..|.---
#     -------------WELCOME-------------
#     ---.|..|..|..|..|..|..|..|..|.---
#     ------.|..|..|..|..|..|..|.------
#     ---------.|..|..|..|..|.---------
#     ------------.|..|..|.------------
#     ---------------.|.---------------
# Input Format

# A single line containing the space separated values of  and .

# Constraints

# Output Format

# Output the design pattern.

# Sample Input

# 9 27
# Sample Output

# ------------.|.------------
# ---------.|..|..|.---------
# ------.|..|..|..|..|.------
# ---.|..|..|..|..|..|..|.---
# ----------WELCOME----------
# ---.|..|..|..|..|..|..|.---
# ------.|..|..|..|..|.------
# ---------.|..|..|.---------
# ------------.|.------------



#############################################################################


from __future__ import print_function

def main():
    a, b = raw_input().split(" ")
    int_a = int(a)
    int_b = int(b)
    halfway = int_a / 2
    welcome = "WELCOME"
    wel_line_number = (((int_a - 5) / 2) - 1) + int_a
    wel_line = "-" * wel_line_number
    first_line_number = (((int_a - 5) / 2) + 1) + int_a
    first_line_dash = "-" * first_line_number 
    dots = ".|."
    dots_number = 1
    if int_a % 2 != 0 and (int_b / int_a == 3) and (5 < int_a < 101) and (15 < int_b < 303):
        
        # FIRST HALF
        i = 0
        while i < halfway:
            print (first_line_dash + (dots * dots_number) + first_line_dash)
            first_line_number = int(first_line_number - 3)
            first_line_dash = "-" * first_line_number
            dots_number += 2
            i += 1
      
           
        # WELCOME LINE
        print (wel_line + welcome + wel_line)
        
        # SECOND HALF
        i = 0
        while i < halfway:
            first_line_number = int(first_line_number + 3)
            first_line_dash = "-" * first_line_number
            dots_number -= 2
            print (first_line_dash + (dots * dots_number) + first_line_dash)
            i += 1
            
    else:
        print ("no")
        return

if __name__ == "__main__":
    main()
    
