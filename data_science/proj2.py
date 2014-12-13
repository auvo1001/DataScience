from __future__ import print_function
import os
import numpy as np
from matplotlib import pyplot as plt

alltext = ""

def splitFile(filename):
    """
    """
    f = open(filename, "r")
    text = f.read()
    f.close()
    i = text.rfind("u'Job Details'")
    S1 = text[i:]
    i = S1.find("naiJQuery")
    S2 = S1[:i]
    #alltext = alltext +  S2
    L =S2.split()
    #print L
    return L

MainDic1 = {"Master":0 ,"PhD":0 ,"MS":0,"SAS":0,"SPSS":0,"Hadoop":0,"Degree":0,"Computational Thinking":0,"Analytics":0,"Hive":0,"Pig":0,"Computer Science":0, "NoSQL":0,"C":0,"C++":0,"Java":0,"JavaScript":0,"AJAX":0,".NET":0,"Oracle":0,"Python":0,"Amazon Web Services":0,"SQL":0,"Social Media":0,"Video":0,"Audio":0,"Picture":0,"R":0,"Information retrieval":0,"Data Mining":0,"Statistics":0,"Machine learning":0}
def NoOfWords(s):
    """
    """
    n =1
    for i in s:
        if i ==" ": n +=1
    return n

def countSkills(filename):
    """
    """
    L= splitFile(filename)
    #print (L)
    for i in range(len(L)):
        s = L[i]
        for skill in MainDic1:
            if ((len(skill) ==1 )) :
                if   skill+"," in s or skill+"/" in s :
                    MainDic1[skill] +=1
            else:
                if ((len(skill) <=3 )):
                    if skill in s:
                        MainDic1[skill] +=1
                else:
                    tmp =""
                    lenOfL =len(L)
                    if NoOfWords(skill) > 1:
                        for k in range(NoOfWords(skill)):
                            if lenOfL-1 >= i+k: tmp += L[i+k] + " "
                        if skill.lower() in tmp.lower():
                            MainDic1[skill] +=1
                    else:
                        if skill.lower() in s.lower():
                            MainDic1[skill] +=1

    #print MainDic1
    return MainDic1



def plot_chart():
    """
    """
    OX = []
    OY = []
    try :
    #with open('data.txt', 'r') as openedFile :
        for i in MainDic1 :
            OY.append(int(MainDic1[i]))
            OX.append(str(i))
    except IOError :
        print("IOError!")



    fig = plt.figure()

    width = 1.5
    ind = np.arange(len(OY))
    plt.bar(ind, OY, 1)
    plt.xticks(ind + width /2  , OX)

    fig.autofmt_xdate()

    plt.savefig("figure.pdf")
    plt.show()





def searchForFiles():
    """
    """

    for file in os.listdir("C:\Users\\a\Google Drive\workspace\DataScience\data_science\data_science\spiders\jobs"):
       if file.endswith(".txt"):
         countSkills(file)
         #print(file)
    cont =MainDic1["MS"]
    MainDic1["Master"] += cont
    del MainDic1["MS"]
    print(MainDic1)
    plot_chart()
