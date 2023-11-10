#!/usr/bin/env python
# coding: utf-8

import random
import time

txt_tables1=[]
f=open("./part.1.txt","r",encoding="utf-8")
line=f.readline()
while line:
    txt_data1=eval(line)
    txt_tables1.append(txt_data1)
    line=f.readline()
    
txt_tables2=[]
f=open("./part.2.txt","r",encoding="utf-8")
line=f.readline()
while line:
    txt_data2=eval(line)
    txt_tables2.append(txt_data2)
    line=f.readline()

txt_tables3=[]
f=open("./part.3.txt","r",encoding="utf-8")
line=f.readline()                                                                   
while line:
    txt_data3=eval(line)
    txt_tables3.append(txt_data3)
    line=f.readline()
    
WORDS1=txt_data1.split(",")
WORDS2=txt_data2.split(",")
WORDS3=txt_data3.split(",")                                                         

scores=0 #Total points scores+=1/2/3
timescores=0
n=0                                                                                   

def jpg():
    maze = [[2,0],[4,0,1,0,4,0]]
    for row in maze:
        for cell in row:
            if cell == 0:
                print("✧",end=" ")
            elif cell == 1:
                print(random.choice(["Nice!","Perfect!","Great!!!","Fantastic!","Good job!!","Ohhhhhhh","Brilliant!"]), end='')
            elif cell == 2:
                print(random.choice(["(｡>∀<｡)","(=^▽^=)"," o(*≧▽≦)ツ ~","\（*^0^*）/","(´▽｀)ノ♪","੭ ᐕ)੭*⁾⁾","Σ(ﾟ∀ﾟﾉ)ﾉ","（★＞U＜★）"]))   
            else:
                print("-"*12,end="")
    print()            
    return print()                                                                    

print("Welcome to Crossword! Please guess a word from the jumbled letters.\nThere are three levels of increasing difficulties. \nYou will get 1 point for guessing one correctly in the first level, 2 points for guessing one correctly in the second level, 3 points for guessing one correctly in the third level. \nThe players who take less time gets extra points, so let's see who get the most in the end!\n")
isContinue1 = "L1"   
while isContinue1 in ("L1","l1"):
    word = random.choice(WORDS1)
    answer = word
    jumble = ""
    for i in word:
        position = random.randrange(len(word))
        jumble+= word[position]        
        word = word[:position] + word[(position+1):]                                  
           
    w1=[]                                                                             
    w1.append(answer)
    wordsnew=set(WORDS1)-set(w1)
    WORDS1=list(wordsnew)
        
    if jumble==answer:
        continue
    else:
        print("The disorganized word is：", jumble)                                             
          
    start1 = time.perf_counter()                                                      
    
    guess = input("Please enter your guessing：")
    print()
    times=0
    while guess != answer:
        times+=1
        guess = input("Wrong! Already guessed it wrong for {0} times, please guess again:".format(times))
        if times==2:
            print("Tips：The first letter of the correct word is:",answer[0],".")
            guess=input("Please guess again accordingly:")
        elif times==4:
            print("Tips：The first two letters of the correct word are:",answer[0],answer[1],".")
            guess=input("Please guess again accordingly:")
        elif times==7:
            print("Already guessed for too many times! lol \nLet me tell you the answer：",answer,".")
            break                                                                     
    else:
        scores+=1                                                                     

        end1 = time.perf_counter()  
        thetime1 = end1-start1
        print("Used time {0:.2f} seconds".format(thetime1))
        print()                                                                       
        if thetime1<3.00:
            timescores+=3
        elif thetime1<5.00:
            timescores+=2
        elif thetime1<10.00:
            timescores+=1 
        print("Congratulations！Current points {0}.".format(scores+timescores))
        jpg()                                                                       
    if scores>=6:
        break                                                                        
        
isContinue2 = input("Continue game？\nIf Yes，please enter L2 for second level; \nIf No，please enter anything else.\n")

if isContinue2 in ("L2","l2"):                                                        
    while scores<18:
        word = random.choice(WORDS2)
        answer = word
        jumble = ""
        for i in word:
            position = random.randrange(len(word))
            jumble += word[position]
            word = word[:position] + word[(position + 1):]                            
         
        w2=[]
        w2.append(answer)
        wordsnew=set(WORDS2)-set(w2)
        WORDS2=list(wordsnew)
        
        if jumble==answer:
            continue
        else:
            print("The disorganized word is：", jumble)
    
        start2 = time.perf_counter()                                                  
    
        guess = input("Please enter your guessing：")
        print()
        times=0
        while guess != answer:
            times+=1
            guess = input("Wrong! Already guessed it wrong for {0} times, please guess again:".format(times))
            if times==2:
                print("Tips: The first letter of the correct word is:",answer[0])
                guess=input("Please guess again accordingly:")
            elif times==4:
                print("Tips: The first two letters of the correct word are：",answer[0],answer[1])
                guess=input("Please guess again accordingly:")
            elif times==6:
                print("Tips: The first three letters of the correct word are：",answer[0],answer[1],answer[2])
                guess=input("Please guess again accordingly:")                                  
            elif times==9:
                print("Already guessed for too many times! lol \nLet me tell you the answer：",answer,".")
                print()
                break                                                                 
        else:
            scores+=2                                                                 

            end2 = time.perf_counter()    
            thetime2 = end2-start2     
            print("Used time {0:.2f} seconds.".format(thetime2))
            print()
            if thetime2<5.00:
                timescores+=3
            elif thetime2<10.00:
                timescores+=2
            elif thetime2<20.00:
                timescores+=1
            print("Congratulations！Current points {0}.".format(scores+timescores))
            jpg()                                                                   
        
    else:
        isContinue3 = input("Continue game？\nIf Yes，please enter L3 for third level;\nIf No，please enter anything else.\n")
        while isContinue3 in ("L3","l3"):                                             
            word = random.choice(WORDS3)
            answer = word
            jumble = ""    
            for i in word:
                position = random.randrange(len(word))
                jumble+= word[position]
                word = word[:position] + word[(position+1):]                          
             
            w3=[]                        
            w3.append(answer)
            wordsnew=set(WORDS3)-set(w3)
            WORDS3=list(wordsnew)
                
            if jumble==answer:
                continue
            else:
                print("The disorganized word is：", jumble)                                     
    
            start3 = time.perf_counter()                                              
        
            guess = input("Please enter your guessing：")
            print()
            times=0
            while guess != answer:
                times+=1
                guess = input("Wrong! Already guessed it wrong for {0} times, please guess again:".format(times))
                if times==2 and guess != answer:
                    print("Tips: The first letter of the correct word is:",answer[0])
                    guess=input("Please guess again accordingly:")
                elif times==4 and guess != answer:
                    print("Tips: The first two letters of the correct word are：",answer[0],answer[1])
                    guess=input("Please guess again accordingly:")
                elif times==6 and guess != answer:
                    print("Tips: The first three letters of the correct word are：",answer[0],answer[1],answer[2])
                    guess=input("Please guess again accordingly:")
                elif times==8 and guess != answer:
                    print("Tips: The first four letters of the correct word are：",answer[0],answer[1],answer[2],answer[3])
                    guess=input("Please guess again accordingly:")                            
                elif times==14 and guess!=answer:
                    print("Already guessed for too many times! lol\nLet me tell you the answer：",answer,".")
                    break                                                           
            else:
                scores+=3                                                           
                    
                end3 = time.perf_counter()
                thetime3 = end3-start3   
                print("Used time {0:.2f} seconds".format(thetime3))     
                print()                                                             
                if thetime3<10.00:
                    timescores+=3
                elif thetime3<20.00:
                    timescores+=2
                elif thetime3<30.00:
                    timescores+=1
                print("Congratulations！Current points {0}.".format(scores+timescores))
                jpg()                                                               
                
            if scores>=36:
                print("Game over and congratulations on passing the final level! Ultimate points {0}. Welcome back next time！".format(scores+timescores))  
                break      
        else:
            print("Congratulations on passing the second level! Ultimate points {0}. Welcome back next time！".format(scores+timescores))
            isContinue="over"   
elif isContinue1 in ("N"):
    print("Congratulations on passing the first level! Ultimate points {0}. Welcome back next time！".format(scores+timescores))
else: print("Congratulations on passing the first level! Ultimate points {0}. Welcome back next time！".format(scores+timescores))
