Lists:

Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Input Format

The first line contains an integer, , denoting the number of commands. 
Each line  of the  subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]

############################################################################

if __name__ == '__main__':
    N = int(raw_input())
    li = []
    nli = []
    for i in range(0, N):
        li = raw_input().split()
        if (li[0] == "insert"):
            nli.insert(int(li[1]), int(li[2]))
            continue
        elif (li[0] == "print"):
            print (nli)
            continue
        elif (li[0] == "remove"):
            nli.remove(int(li[1]))
            continue
        elif (li[0] == "append"):
            nli.append(int(li[1]))
            continue
        elif (li[0] == "sort"):
            nli = map(int, nli)
            nli.sort()
            continue
        elif (li[0] == "pop"):
            nli.pop()
            continue
        elif (li[0] == "reverse"):
            nli.reverse()
            continue
        
