from django.shortcuts import render
import random
import time

txt_tables1 = []

txt_tables2 = []
txt_tables3 = []
txt_data1=""
txt_data2=""
txt_data3=""
scores=0 #Total points scores+=1/2/3
timescores=0
n=0
def getWordOne():
    global txt_data1
    txt_tables1 = []
    f = open("part.1.txt", "r", encoding="utf-8")
    line = f.readline()
    while line:
        txt_data1 = eval(line)
        txt_tables1.append(txt_data1)
        line = f.readline()
def getWordTwo():
    global txt_data2
    f = open("part.2.txt", "r", encoding="utf-8")
    line = f.readline()
    while line:
        txt_data2 = eval(line)
        txt_tables2.append(txt_data2)
        line = f.readline()
def getWordThree():
    global txt_data3
    txt_tables3 = []
    f = open("part.3.txt", "r", encoding="utf-8")
    line = f.readline()
    while line:
        txt_data3 = eval(line)
        txt_tables3.append(txt_data3)
        line = f.readline()
    print(txt_data3)

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


# Create your views here.
def startGame(request):
    return render(request,"startGame.html")
start1=0
def beginGame(request):
    scores = request.GET.get("scores")
    timescores=request.GET.get("timescores")
    print(scores, "   ",timescores)
    flag=0
    if not scores:
        scores=0
        flag=1
        timescores =0
    getWordOne()
    WORDS1 = txt_data1.split(",")
    # print(WORDS1)
    while True:
        word = random.choice(WORDS1)
        answer = word
        print(answer)
        jumble = ""
        for i in word:
            position = random.randrange(len(word))
            jumble += word[position]
            word = word[:position] + word[(position + 1):]

        w1 = []
        w1.append(answer)
        wordsnew = set(WORDS1) - set(w1)
        WORDS1 = list(wordsnew)

        if jumble == answer:
            continue
        else:
            print("The disorganized word is：", jumble)
            break
    return render(request, "levelOne.html", {"jumble": jumble, "answer": answer,"scores":scores,"flag":flag,"timescores":timescores})

def guessTwo(request):
    scores = request.GET.get("scores")

    if not scores:
        scores = 0
    else:
        scores=int(scores)
    timescores=request.GET.get("timescores")
    getWordTwo()
    WORDS2 = txt_data2.split(",")
    jumble = ""
    answer=""
    while scores < 18:
        word = random.choice(WORDS2)
        answer = word
        print(answer)

        for i in word:
            position = random.randrange(len(word))
            jumble += word[position]
            word = word[:position] + word[(position + 1):]

        w2 = []
        w2.append(answer)
        wordsnew = set(WORDS2) - set(w2)
        WORDS2 = list(wordsnew)
        # print(WORDS2,"---------------")
        if jumble == answer:
            jumble = ""
            continue
        else:
            print("The disorganized word is：", jumble)
            break
    return render(request, "levelTwo.html", {"jumble": jumble, "answer": answer,"scores":scores,"timescores":timescores})
def guessThree(request):
    getWordThree()
    WORDS3 = txt_data3.split(",")
    scores = request.GET.get("scores")
    timescores = request.GET.get("timescores")
    if not scores:
        scores = 0
        timescores=0
    else:
        scores = int(scores)

    while True:
        word = random.choice(WORDS3)
        answer = word
        print(answer)
        jumble = ""
        for i in word:
            position = random.randrange(len(word))
            jumble += word[position]
            word = word[:position] + word[(position + 1):]

        w3 = []
        w3.append(answer)
        wordsnew = set(WORDS3) - set(w3)
        WORDS3 = list(wordsnew)

        if jumble == answer:
            continue
        else:
            print("The disorganized word is：", jumble)
            break
    return render(request, "levelThree.html", {"jumble": jumble, "answer": answer,"scores":scores,"timescores":timescores})
def backMain(request):
    return render(request,"startGame.html")
