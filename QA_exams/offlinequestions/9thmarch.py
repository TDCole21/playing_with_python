#!/usr/bin/env python3.8

def evenNumbers(min, max):
    answer=""
    for i in range(min,max+1):
        i = str(i)
        numberlen=len(i)
        talley=0
        for char in i:
            if int(char) % 2 == 0:
                talley=talley+1
            if talley == numberlen:
                answer = answer + str(i) + ", "
    if answer[-2] == "," and answer[-1] == " ":
        answer=answer[0:-2]




    print(answer)

evenNumbers(1000,3000)