
import telebot
from telebot import types
import math
API_TOKEN="1844883186:AAHS-wqGST-ryVd-FkVmWMzb6P0q9Xwa67w"
bot = telebot.TeleBot(API_TOKEN, parse_mode=None) 

def solve(inputCounter,message,tjk):
    try:
        allnumber=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        numbers=inputCounter.split("-")
        if len(numbers) ==1:
            numbers=numbers[0].split(",")
        if len(numbers) ==1:
            numbers=numbers[0].split(".")
        if len(numbers) ==1:
            numbers=numbers[0].split("&")
        if len(numbers) ==1:
            numbers=numbers[0].split("/")
        present={0:"0000",1:"0001",2:"0010",3:"0011",4:"0100",5:"0101",6:"0110",7:"0111",8:"1000",9:"1001",10:"1010",11:"1011",12:"1100",13:"1101",14:"1110",15:"1111"}
        next={0:"xxxx",1:"xxxx",2:"xxxx",3:"xxxx",4:"xxxx",5:"xxxx",6:"xxxx",7:"xxxx",8:"xxxx",9:"xxxx",10:"xxxx",11:"xxxx",12:"xxxx",13:"xxxx",14:"xxxx",15:"xxxx"}

        xx = list(present[0])
        for xx in numbers:
            index=numbers.index(xx)
            if index==(len(numbers)-1):
                index=-1
            c=bin(int(numbers[index+1])).replace("0b", "")
            if c=="0":
                c="0000"
            elif c=="1":
                c="0001"
            elif c=="10":
                c="0010"
            elif c=="1":
                c="0001"
            elif c=="11":
                c="0011"
            elif c=="100":
                c="0100"
            elif c=="101":
                c="0101"
            elif c=="110":
                c="0110" 
            elif c=="111":
                c="0111"  
            next[int(xx)]=c

        def split(dd,n,nn):
            return list(dd[n])[nn]

        ###########################
        from prettytable import PrettyTable

        A = PrettyTable(['00', '01','11', '10'])
        A.add_row([split(next,0,0), split(next,4,0),split(next,12,0),split(next,8,0)])
        A.add_row([split(next,1,0), split(next,5,0),split(next,13,0),split(next,9,0)])
        A.add_row([split(next,3,0), split(next,7,0),split(next,15,0),split(next,11,0)])
        A.add_row([split(next,2,0), split(next,6,0),split(next,14,0),split(next,10,0)])
        B = PrettyTable(['00', '01','11', '10'])
        B.add_row([split(next,0,1), split(next,4,1),split(next,12,1),split(next,8,1)])
        B.add_row([split(next,1,1), split(next,5,1),split(next,13,1),split(next,9,1)])
        B.add_row([split(next,3,1), split(next,7,1),split(next,15,1),split(next,11,1)])
        B.add_row([split(next,2,1), split(next,6,1),split(next,14,1),split(next,10,1)])
        C = PrettyTable(['00', '01','11', '10'])
        C.add_row([split(next,0,2), split(next,4,2),split(next,12,2),split(next,8,2)])
        C.add_row([split(next,1,2), split(next,5,2),split(next,13,2),split(next,9,2)])
        C.add_row([split(next,3,2), split(next,7,2),split(next,15,2),split(next,11,2)])
        C.add_row([split(next,2,2), split(next,6,2),split(next,14,2),split(next,10,2)])
        D= PrettyTable(['00', '01','11', '10'])
        D.add_row([split(next,0,3), split(next,4,3),split(next,12,3),split(next,8,3)])
        D.add_row([split(next,1,3), split(next,5,3),split(next,13,3),split(next,9,3)])
        D.add_row([split(next,3,3), split(next,7,3),split(next,15,3),split(next,11,3)])
        D.add_row([split(next,2,3), split(next,6,3),split(next,14,3),split(next,10,3)])
        ###############################

        taList=[]
        taList2=[]
        tbList2=[]
        tcList2=[]
        tdList2=[]
        ta1=[]
        tad=[]
        tb1=[]
        tbd=[]
        tc1=[]
        tcd=[]
        td1=[]
        tdd=[]

        if (tjk=="T"):
            for tal in range (0,16):
                xtal=split(next,tal,0)
                if tal>=8:
                    if xtal=="0":
                        xtal="1"
                    elif xtal=="1":
                        xtal="0"
                taList.append(xtal)
                taList2.append(xtal)

            for tt in taList2:
                if tt=="1":
                    ta1.append(taList2.index(tt))
                    taList2[taList2.index(tt)]=""
                elif tt=="x":
                    tad.append(taList2.index(tt))
                    taList2[taList2.index(tt)]=""

            tbList=[]

            for tal in range (0,16):
                xtal=split(next,tal,1)
                if tal in [4,5,6,7,12,13,15,14]:
                    if xtal=="0":
                        xtal="1"
                    elif xtal=="1":
                        xtal="0"
                tbList.append(xtal)
                tbList2.append(xtal)
            for tt in tbList2:
                if tt=="1":
                    tb1.append(tbList2.index(tt))
                    tbList2[tbList2.index(tt)]=""
                elif tt=="x":
                    tbd.append(tbList2.index(tt))
                    tbList2[tbList2.index(tt)]=""

            tcList=[]
            for tal in range (0,16):
                xtal=split(next,tal,2)
                if tal in [3,7,15,11,2,6,14,10]:
                    if xtal=="0":
                        xtal="1"
                    elif xtal=="1":
                        xtal="0"
                tcList.append(xtal)
                tcList2.append(xtal)
            for tt in tcList2:
                if tt=="1":
                    tc1.append(tcList2.index(tt))
                    tcList2[tcList2.index(tt)]=""
                elif tt=="x":
                    tcd.append(tcList2.index(tt))
                    tcList2[tcList2.index(tt)]=""
            tdList=[]
            for tal in range (0,16):
                xtal=split(next,tal,3)
                if tal in [1,5,13,9,3,7,15,11]:
                    if xtal=="0":
                        xtal="1"
                    elif xtal=="1":
                        xtal="0"
                tdList.append(xtal)
                tdList2.append(xtal)
            for tt in tdList2:
                if tt=="1":
                    td1.append(tdList2.index(tt))
                    tdList2[tdList2.index(tt)]=""
                elif tt=="x":
                    tdd.append(tdList2.index(tt))
                    tdList2[tdList2.index(tt)]=""

        elif (tjk=="J"):
            for tal in range (0,16):
                xtal=split(next,tal,0)
                if tal>=8:
                    if xtal=="0":
                        xtal="x"
                    elif xtal=="1":
                        xtal="x"
                taList.append(xtal)
                taList2.append(xtal)

            for tt in taList2:
                if tt=="1":
                    ta1.append(taList2.index(tt))
                    taList2[taList2.index(tt)]=""
                elif tt=="x":
                    tad.append(taList2.index(tt))
                    taList2[taList2.index(tt)]=""

            tbList=[]

            for tal in range (0,16):
                xtal=split(next,tal,1)
                if tal in [4,5,6,7,12,13,15,14]:
                    if xtal=="0":
                        xtal="x"
                    elif xtal=="1":
                        xtal="x"
                tbList.append(xtal)
                tbList2.append(xtal)
            for tt in tbList2:
                if tt=="1":
                    tb1.append(tbList2.index(tt))
                    tbList2[tbList2.index(tt)]=""
                elif tt=="x":
                    tbd.append(tbList2.index(tt))
                    tbList2[tbList2.index(tt)]=""

            tcList=[]
            for tal in range (0,16):
                xtal=split(next,tal,2)
                if tal in [3,7,15,11,2,6,14,10]:
                    if xtal=="0":
                        xtal="x"
                    elif xtal=="1":
                        xtal="x"
                tcList.append(xtal)
                tcList2.append(xtal)
            for tt in tcList2:
                if tt=="1":
                    tc1.append(tcList2.index(tt))
                    tcList2[tcList2.index(tt)]=""
                elif tt=="x":
                    tcd.append(tcList2.index(tt))
                    tcList2[tcList2.index(tt)]=""
            tdList=[]
            for tal in range (0,16):
                xtal=split(next,tal,3)
                if tal in [1,5,13,9,3,7,15,11]:
                    if xtal=="0":
                        xtal="x"
                    elif xtal=="1":
                        xtal="x"
                tdList.append(xtal)
                tdList2.append(xtal)
            for tt in tdList2:
                if tt=="1":
                    td1.append(tdList2.index(tt))
                    tdList2[tdList2.index(tt)]=""
                elif tt=="x":
                    tdd.append(tdList2.index(tt))
                    tdList2[tdList2.index(tt)]=""

        elif (tjk=="K"):
            for tal in range (0,16):
                xtal=split(next,tal,0)
                if tal>=8:
                    if xtal=="0":
                        xtal="1"
                    elif xtal=="1":
                        xtal="0"
                else:
                    if xtal=="0":
                        xtal="x"
                    elif xtal=="1":
                        xtal="x"
                
                taList.append(xtal)
                taList2.append(xtal)

            for tt in taList2:
                if tt=="1":
                    ta1.append(taList2.index(tt))
                    taList2[taList2.index(tt)]=""
                elif tt=="x":
                    tad.append(taList2.index(tt))
                    taList2[taList2.index(tt)]=""

            tbList=[]

            for tal in range (0,16):
                xtal=split(next,tal,1)
                if tal in [4,5,6,7,12,13,15,14]:
                    if xtal=="0":
                        xtal="1"
                    elif xtal=="1":
                        xtal="0"
                else:
                    if xtal=="0":
                        xtal="x"
                    elif xtal=="1":
                        xtal="x"
                
                tbList.append(xtal)
                tbList2.append(xtal)
            for tt in tbList2:
                if tt=="1":
                    tb1.append(tbList2.index(tt))
                    tbList2[tbList2.index(tt)]=""
                elif tt=="x":
                    tbd.append(tbList2.index(tt))
                    tbList2[tbList2.index(tt)]=""

            tcList=[]
            for tal in range (0,16):
                xtal=split(next,tal,2)
                if tal in [3,7,15,11,2,6,14,10]:
                    if xtal=="0":
                        xtal="1"
                    elif xtal=="1":
                        xtal="0"
                else:
                    if xtal=="0":
                        xtal="x"
                    elif xtal=="1":
                        xtal="x"
                
                tcList.append(xtal)
                tcList2.append(xtal)
            for tt in tcList2:
                if tt=="1":
                    tc1.append(tcList2.index(tt))
                    tcList2[tcList2.index(tt)]=""
                elif tt=="x":
                    tcd.append(tcList2.index(tt))
                    tcList2[tcList2.index(tt)]=""
            tdList=[]
            for tal in range (0,16):
                xtal=split(next,tal,3)
                if tal in [1,5,13,9,3,7,15,11]:
                    if xtal=="0":
                        xtal="1"
                    elif xtal=="1":
                        xtal="0"
                else:
                    if xtal=="0":
                        xtal="x"
                    elif xtal=="1":
                        xtal="x"
                
                tdList.append(xtal)
                tdList2.append(xtal)
            for tt in tdList2:
                if tt=="1":
                    td1.append(tdList2.index(tt))
                    tdList2[tdList2.index(tt)]=""
                elif tt=="x":
                    tdd.append(tdList2.index(tt))
                    tdList2[tdList2.index(tt)]=""
        ################################
        presenttable = PrettyTable(['A', 'B','C', 'D'])
        presenttable.add_row([split(present,0,0),split(present,0,1),split(present,0,2),split(present,0,3)])
        presenttable.add_row([split(present,1,0),split(present,1,1),split(present,1,2),split(present,1,3)])    
        presenttable.add_row([split(present,2,0),split(present,2,1),split(present,2,2),split(present,2,3)])
        presenttable.add_row([split(present,3,0),split(present,3,1),split(present,3,2),split(present,3,3)])
        presenttable.add_row([split(present,4,0),split(present,4,1),split(present,4,2),split(present,4,3)])
        presenttable.add_row([split(present,5,0),split(present,5,1),split(present,5,2),split(present,5,3)])
        presenttable.add_row([split(present,6,0),split(present,6,1),split(present,6,2),split(present,6,3)])
        presenttable.add_row([split(present,7,0),split(present,7,1),split(present,7,2),split(present,7,3)])
        presenttable.add_row([split(present,8,0),split(present,8,1),split(present,8,2),split(present,8,3)])
        presenttable.add_row([split(present,9,0),split(present,9,1),split(present,9,2),split(present,9,3)])
        presenttable.add_row([split(present,10,0),split(present,10,1),split(present,10,2),split(present,10,3)])
        presenttable.add_row([split(present,11,0),split(present,11,1),split(present,11,2),split(present,11,3)])
        presenttable.add_row([split(present,12,0),split(present,12,1),split(present,12,2),split(present,12,3)])
        presenttable.add_row([split(present,13,0),split(present,13,1),split(present,13,2),split(present,13,3)])
        presenttable.add_row([split(present,14,0),split(present,14,1),split(present,14,2),split(present,14,3)])
        presenttable.add_row([split(present,15,0),split(present,15,1),split(present,15,2),split(present,15,3)])
            ##################################
        nexttable = PrettyTable(['A+', 'B+','C+', 'D+'])
        nexttable.add_row([split(next,0,0),split(next,0,1),split(next,0,2),split(next,0,3)])
        nexttable.add_row([split(next,1,0),split(next,1,1),split(next,1,2),split(next,1,3)])    
        nexttable.add_row([split(next,2,0),split(next,2,1),split(next,2,2),split(next,2,3)])
        nexttable.add_row([split(next,3,0),split(next,3,1),split(next,3,2),split(next,3,3)])
        nexttable.add_row([split(next,4,0),split(next,4,1),split(next,4,2),split(next,4,3)])
        nexttable.add_row([split(next,5,0),split(next,5,1),split(next,5,2),split(next,5,3)])
        nexttable.add_row([split(next,6,0),split(next,6,1),split(next,6,2),split(next,6,3)])
        nexttable.add_row([split(next,7,0),split(next,7,1),split(next,7,2),split(next,7,3)])
        nexttable.add_row([split(next,8,0),split(next,8,1),split(next,8,2),split(next,8,3)])
        nexttable.add_row([split(next,9,0),split(next,9,1),split(next,9,2),split(next,9,3)])
        nexttable.add_row([split(next,10,0),split(next,10,1),split(next,10,2),split(next,10,3)])
        nexttable.add_row([split(next,11,0),split(next,11,1),split(next,11,2),split(next,11,3)])
        nexttable.add_row([split(next,12,0),split(next,12,1),split(next,12,2),split(next,12,3)])
        nexttable.add_row([split(next,13,0),split(next,13,1),split(next,13,2),split(next,13,3)])
        nexttable.add_row([split(next,14,0),split(next,14,1),split(next,14,2),split(next,14,3)])
        nexttable.add_row([split(next,15,0),split(next,15,1),split(next,15,2),split(next,15,3)])
            ##################################
        TA =PrettyTable(['00', '01','11', '10'])
        TA.add_row([taList[0], taList[4],taList[12],taList[8]])
        TA.add_row([taList[1], taList[5],taList[13],taList[9]])
        TA.add_row([taList[3], taList[7],taList[15],taList[11]])
        TA.add_row([taList[2], taList[6],taList[14],taList[10]])
        TB = PrettyTable(['00', '01','11', '10'])
        TB.add_row([tbList[0], tbList[4],tbList[12],tbList[8]])
        TB.add_row([tbList[1], tbList[5],tbList[13],tbList[9]])
        TB.add_row([tbList[3], tbList[7],tbList[15],tbList[11]])
        TB.add_row([tbList[2], tbList[6],tbList[14],tbList[10]])
        TC = PrettyTable(['00', '01','11', '10'])
        TC.add_row([tcList[0], tcList[4],tcList[12],tcList[8]])
        TC.add_row([tcList[1], tcList[5],tcList[13],tcList[9]])
        TC.add_row([tcList[3], tcList[7],tcList[15],tcList[11]])
        TC.add_row([tcList[2], tcList[6],tcList[14],tcList[10]])
        TD = PrettyTable(['00', '01','11', '10'])
        TD.add_row([tdList[0], tdList[4],tdList[12],tdList[8]])
        TD.add_row([tdList[1], tdList[5],tdList[13],tdList[9]])
        TD.add_row([tdList[3], tdList[7],tdList[15],tdList[11]])
        TD.add_row([tdList[2], tdList[6],tdList[14],tdList[10]])
        Tf =PrettyTable(['/', 'Q=0','Q=1'])
        Tf.add_row(["T","N.C","Toggle"])
        
        ###########################
        JA =PrettyTable(['00', '01','11', '10'])
        JA.add_row([taList[0], taList[4],taList[12],taList[8]])
        JA.add_row([taList[1], taList[5],taList[13],taList[9]])
        JA.add_row([taList[3], taList[7],taList[15],taList[11]])
        JA.add_row([taList[2], taList[6],taList[14],taList[10]])
        JB = PrettyTable(['00', '01','11', '10'])
        JB.add_row([tbList[0], tbList[4],tbList[12],tbList[8]])
        JB.add_row([tbList[1], tbList[5],tbList[13],tbList[9]])
        JB.add_row([tbList[3], tbList[7],tbList[15],tbList[11]])
        JB.add_row([tbList[2], tbList[6],tbList[14],tbList[10]])
        JC = PrettyTable(['00', '01','11', '10'])
        JC.add_row([tcList[0], tcList[4],tcList[12],tcList[8]])
        JC.add_row([tcList[1], tcList[5],tcList[13],tcList[9]])
        JC.add_row([tcList[3], tcList[7],tcList[15],tcList[11]])
        JC.add_row([tcList[2], tcList[6],tcList[14],tcList[10]])
        JD = PrettyTable(['00', '01','11', '10'])
        JD.add_row([tdList[0], tdList[4],tdList[12],tdList[8]])
        JD.add_row([tdList[1], tdList[5],tdList[13],tdList[9]])
        JD.add_row([tdList[3], tdList[7],tdList[15],tdList[11]])
        JD.add_row([tdList[2], tdList[6],tdList[14],tdList[10]])
        Jf =PrettyTable(['/', 'Q=0','Q=1'])
        Jf.add_row(["J","N.C","x"])
        Jf.add_row(["K","x","Toggle"])
        #############################################
        KA =PrettyTable(['00', '01','11', '10'])
        KA.add_row([taList[0], taList[4],taList[12],taList[8]])
        KA.add_row([taList[1], taList[5],taList[13],taList[9]])
        KA.add_row([taList[3], taList[7],taList[15],taList[11]])
        KA.add_row([taList[2], taList[6],taList[14],taList[10]])
        KB = PrettyTable(['00', '01','11', '10'])
        KB.add_row([tbList[0], tbList[4],tbList[12],tbList[8]])
        KB.add_row([tbList[1], tbList[5],tbList[13],tbList[9]])
        KB.add_row([tbList[3], tbList[7],tbList[15],tbList[11]])
        KB.add_row([tbList[2], tbList[6],tbList[14],tbList[10]])
        KC = PrettyTable(['00', '01','11', '10'])
        KC.add_row([tcList[0], tcList[4],tcList[12],tcList[8]])
        KC.add_row([tcList[1], tcList[5],tcList[13],tcList[9]])
        KC.add_row([tcList[3], tcList[7],tcList[15],tcList[11]])
        KC.add_row([tcList[2], tcList[6],tcList[14],tcList[10]])
        KD = PrettyTable(['00', '01','11', '10'])
        KD.add_row([tdList[0], tdList[4],tdList[12],tdList[8]])
        KD.add_row([tdList[1], tdList[5],tdList[13],tdList[9]])
        KD.add_row([tdList[3], tdList[7],tdList[15],tdList[11]])
        KD.add_row([tdList[2], tdList[6],tdList[14],tdList[10]])
        #------------------------------------------------------------------------------------------------

        def kmap (termm,dont):
            inputs=['A','B','C','D']                                  # Put the values that F=1 in the Terms List
            terms=termm         # the terms equal to 1
            d=dont                                                       # Dont care list
            op='F'                                                        # the output name
            class term:
                def __init__(self,x,l):
                    self.prime=True
                    self.m=[x]
                    self.val=bin(x)[2:]
                    while(len(self.val)<l):
                        self.val='0'+self.val
                    self.ones=self.val.count('1')
                    
                def hd(self,x):
                    hd,pos=0,0
                    for i in range(len(x.val)):
                        if(self.val[i]!=x.val[i]):
                            hd+=1
                            pos=i
                        if(hd>1):
                            return -1
                    if(hd==1 and (x.val.find('-')==self.val.find('-'))):
                        return pos
                    else:
                        return -1
                        
                def msIn(self,x):
                    ret=[]
                    for i in self.m:
                        if(i in x):
                            ret+=[i]
                    return ret,len(ret)
                                    
                def __str__(self):
                    return self.val
                
                def __eq__(self, x):
                    return self.val == x.val
                    
                def __lt__(self,x):
                    return self.m < x.m

            def setTerms(terms,inputs):
                fo=(len(terms),len(inputs))
                for i in range(fo[0]):
                    terms.append(term(terms[i],fo[1]))
                return terms[int(len(terms)/2):]

            def combineTerms(x):#O(n^2 +n) :( 
                ret=[]
                for i in x:
                    for j in x:
                        buf=i.hd(j)
                        if((buf!=-1) and (j.ones-i.ones==1)):
                            i.prime=False
                            j.prime=False
                            fo=list(i.val)
                            v=term(1,4)
                            v.m=[]
                            #for k in i.m: v.m.append(k)
                            v.m+=i.m
                            #for k in j.m: v.m.append(k)
                            v.m+=j.m
                            fo[buf]='-'
                            v.val=''.join(fo)
                            v.ones=v.val.count('1')
                            ret.append(v)
                for i in x:
                    if i.prime==True:
                        ret.append(i)
                return ret

            def lettersFromBinary(x):
                ret=''
                for i in range(len(x)):
                    if(x[i]=='0'):
                        #ret+='~'+inputs[i]+'.'
                        ret+=inputs[i]+'`'+'.'
                    elif(x[i]=='1'):
                        ret+=inputs[i]+'.'
                return ret[:len(ret)-1]
                
            def result(x):
                buf=''
                for i in x:
                    fo = lettersFromBinary(i.val)
                    if(fo !=''):
                        buf+= fo+' + ' 
                return buf[:len(buf)-3]
            def sizeImpl(x):
                while(True):
                    buf=combineTerms(x)
                    if(x == buf):
                        break
                    x=buf
                return x
                
            def getGroups(x):
                buf=list(x)
                for i in range(len(x)):
                    if (x.count(x[i]) == 2) and x[i].val!='':
                        x[i].val=''
                        buf.remove(x[i])
                return buf
                
            def primeTable(x):
                ms={}
                ret=[]
                for i in x:
                    for k in i.m:
                        try:
                            ms[k].append(i)
                        except:
                            ms[k]=[i]
            
                for i in ms:
                    if(len(ms[i])==1 and i not in d):
                        for j in ms[i]:
                            if(j not in ret):
                                ret.append(j)
                for i in ret:
                    for j in i.m: ms.pop(j,None)
                for i in d:
                    ms.pop(i,None)
                    
                while(len(ms)!=0):
                    currentLength,currentGroups,prime=0,0,0
                    for i in ms:
                        for j in ms[i]:
                            nextGroups,nextLength=j.msIn(ms.keys())
                            if(nextLength>currentLength):
                                currentLength=nextLength
                                currentGroups=nextGroups
                                prime=j
                    ret.append(prime)
                    for i in currentGroups:
                        ms.pop(i,None)

                return ret
            terms+=d
            x=primeTable(getGroups(sizeImpl(setTerms(terms,inputs))))
            return str(result(x))



        ###########################
        aa=kmap(ta1,tad)
        bb=kmap(tb1,tbd)
        cc=kmap(tc1,tcd)
        dd=kmap(td1,tdd)
        numanddlist=[]
        if dd=="":
            dd="1"
        if aa=="":
            aa="1"
        if bb=="":
            bb="1"
        if cc=="":
            cc="1"

        def countorand(v):
            c=0
            ssg=[]
            a2=[]
            a1=v.replace("."," & ").split(" + ")
            na1=len(a1)
            numandd=0
            if na1!=1:
                ssg.append("\n::{} input in OR ::\n".format(na1))   
            for n in a1:
                c+=1
                if (len(n)==1) or (("`" in n) and len(n)==2 ):

                    ssg.append("input {} :: {} ".format(c,n.strip()))
                else:
                    ssg.append("input {} :: {} input in AND".format(c,n.strip()))
                    numandd+=1
            numanddlist.append(numandd)
            s="\n"
            ssgs=s.join(ssg)
            return ssgs
            

        a00=countorand(aa)  
        a11=countorand(bb) 
        a22=countorand(cc)  
        a33=countorand(dd) 
        z=0
        for n in numanddlist:
            z+=n
        
        ######################
        return presenttable,nexttable,A,B,C,D,TA,TB,TC,TD,aa,bb,cc,dd,Tf,a00,a11,a22,a33,z,JA,JB,JC,JD,KA,KB,KC,KD,Jf
    except:
        if message.text=="/upgrade" or message.text=="/start":
            start(message)
        else:
            bot.send_message(message.chat.id ,"❌❌❌\nThe entry was made by mistake.\nPlease wait a few moments, and we will send you a message again to enter the counter code 🔄.\n\n⚠️⚠️⚠️\nMake sure that the code number is correct, and between the numbers there is a sign (- / , &).\n\n❌❌❌\nتم الادخال بطريقه خطأ برجاء الانتظار لحظات و سنرسل اليك رساله من جديد لادخال كود العداد .\nتاكد من ان رقم الكود صحيح و بين الارقام علامه من هذه العلامات (- / , &).")


listproject=types.ReplyKeyboardMarkup(row_width=1)
p1=types.KeyboardButton("0-1-4-6-8-9-12-14-15-0")
p2=types.KeyboardButton("0-2-4-5-9-12-15-0")
p3=types.KeyboardButton("0-2-4-6-8-10-12-13-14-15-0")
p4=types.KeyboardButton("0-3-4-5-8-9-10-0")
p5=types.KeyboardButton("0-3-4-5-8-9-11-14-15-0")
p6=types.KeyboardButton("0-3-5-6-9-11-13-15-0")
p7=types.KeyboardButton("0-3-5-9-10-11-12-15-0")
p8=types.KeyboardButton("0-3-6-9-11-12-13-14-15-0")
p9=types.KeyboardButton("0-5-8-9-12-13-14-15-0")
p10=types.KeyboardButton("1-2-3-4-7-8-9-12-14-1")
p11=types.KeyboardButton("1-2-3-5-6-8-9-12-1")
p12=types.KeyboardButton("1-2-3-7-8-9-10-11-12-13-15-1")
p13=types.KeyboardButton("1-3-5-7-9-11-12-13-14-15-1")
p14=types.KeyboardButton("1-4-5-7-8-12-13-15-1")
p15=types.KeyboardButton("2-3-4-5-6-9-12-14-15-2")
p16=types.KeyboardButton("2-4-6-7-8-9-11-13-14-15-2")
p17=types.KeyboardButton("3-5-6-8-9-11-14-15-3")
p18=types.KeyboardButton("4-5-6-11-12-13-14-15-4")
p19=types.KeyboardButton("6-7-8-9-10-11-13-14-15-6")
p20=types.KeyboardButton("6-8-9-10-11-12-13-14-15-6")
back=types.KeyboardButton("🔙 BACK")
back2=types.KeyboardButton("🔙  BACK")
listproject.add(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,back)
loginn=types.ReplyKeyboardMarkup(row_width=1)
loginn1=types.KeyboardButton("List Of Projects 📽")
loginn2=types.KeyboardButton("Another Counter ⏳")
loginn.add(loginn1,loginn2,back2)
keyboard=types.ReplyKeyboardMarkup(row_width=1)
item1=types.KeyboardButton("Login 🔐")
keyboard.add(item1)
inline=types.InlineKeyboardMarkup(row_width=2)
it1=types.InlineKeyboardButton("Counter Tutorial",url="https://www.youtube.com/watch?v=s-o3jU_16wk")
it2=types.InlineKeyboardButton("Design Counter Proteus",url="https://www.youtube.com/watch?v=akkAjytWCKs")
inline.add(it1)
inline.add(it2)
@bot.message_handler(commands=['start','upgrade'])
def start(message):
    enstart="*Welcome and we are glad to know you ❤️\.\n\n⚠️⚠️ Note: \n\n1️⃣ This bot is for educational use only and the developer is not affiliated with any other use ✏️\. \n\n2️⃣ All messages between the user and the developer have been encrypted from entering until the completion of the resolution process, just to ensure the best service for you 💌\.*"
    bot.send_message(message.chat.id,enstart,parse_mode="MarkdownV2",reply_markup=keyboard)
    arstart="* مرحبا بك,سررنا لمعرفتك\.❤️ \n\n⚠️⚠️ ملحوظه:\n\n1️⃣ هذا البوت للغرض التعليمي فقط و المطور لا علاقه له باي استخدام اخر✏️\.\n\n2️⃣ تم تشفير جميع الرسائل بين المستخدم و المطور من الدخول حتي اتمام عمليه الحل فقط لضمان لفضل خدمه لك💌\.*"
    bot.send_message(message.chat.id,arstart,parse_mode="MarkdownV2")
    use="""طريقه استخدام البوت :
1. اضغط علي الزر login و ادخل كلمه المرور للدخول ثم ادخل رقم ال counter الخاص بك كما اهو في الجدول ثم سيظهر لك خطوات الحل صحيحه و دقيقه بنسبه تفوق ال 95%
2. عند الدخول ستجد قائمة من ثلاث خانات ::
ا - (List Of Projects 📽) : ستجد بيها 20 كود للعدادات ( تقريبا جميع الاكواد ).  
ب - (Another Counter ⏳) : يمكنك ادخال اي من الاكواد الاخري الغير موجوده ف القائمة السابقه.
ج - (🔙 BACK) : للرجوع الي القائمه الدخول من جديد."""
    useen="""How to use the bot:
1. Press the login button and enter the password to enter, then enter your counter number as it is in the table, then the correct and accurate solution steps will appear for you, at a rate of more than 95%
2. After login, you will find a list of three fields:
    A - (List Of Projects 📽): In it, you will find 20 code for counters (almost all codes).
    B - (Another Counter ⏳): You can enter any of the other codes not present in the previous list.
    C - (🔙 BACK): To return to the menu, login again."""

    bot.send_message(message.chat.id,use)
    bot.send_message(message.chat.id,useen)
    msgg="Name : "+str(message.from_user.first_name)+" "+str(message.from_user.last_name)+"\n\n@"+str(message.from_user.username)
    bot.send_message(1109158839,msgg)

@bot.message_handler(regexp="Login 🔐")
def login (message):
    msg = bot.reply_to(message, '`Enter Password : `',parse_mode="MarkdownV2")
    bot.register_next_step_handler(msg, check)
def solu (message):
    msg=bot.send_message(message.chat.id,"`Enter counter : `",parse_mode="MarkdownV2")
    bot.register_next_step_handler(msg, step1)
def check (message):
    if (message.text=="jy3Q4MVjgP+dsg6B"):
        bot.send_message(message.chat.id,"🔓 Password is Correct  ✅",reply_markup=loginn)
    elif message.text=="/upgrade" or message.text=="/start":
        start(message)
    elif message.text=="Login 🔐":
        login(message)
    else:
        msg=bot.send_message(message.chat.id,"`incorrect password ❌\nEnter Password again :`",parse_mode="MarkdownV2")
        bot.register_next_step_handler(msg, check)

def step1 (message):
    try:
        ss=0
        presenttable,nexttable,A,B,C,D,TA,TB,TC,TD,aa,bb,cc,dd,Tf,a00,a11,a22,a33,z,JA,JB,JC,JD,KA,KB,KC,KD,Jf= solve(message.text[:-2],message,"T")
        msgstate="State Table : "+"\n\n"+"1️⃣ Present State :\n"+str(presenttable)+"\n\n2️⃣ Next State :\n"+str(nexttable)
        bot.send_message(message.chat.id,msgstate)
        msga="Next State K-MAP : \n\nA+ :\n"+str(A)+"\n\nB+ : \n"+str(B)+"\n\nC+ : \n"+str(C)+"\n\nD+ :\n"+str(D)+"\n\n"
        bot.send_message(message.chat.id,msga)
        msgb="FLIP-FLOP K-MAP : \n\n"+"Using T-Flip-Flop :\n"+str(Tf)+"\n\n"+"TA :\n"+str(TA)+"\nTA = "+aa+"\n\nTB : \n"+str(TB)+"\nTB = "+bb+"\n\nTC : \n"+str(TC)+"\nTC = "+cc+"\n\nTD :\n"+str(TD)+"\nTD = "+dd+"\n\n"
        bot.send_message(message.chat.id,msgb)
        msgc="DESIGN :\n\nTA :\n"+a00+"\n\nTB :\n"+a11+"\n\nTC :\n"+a22+"\n\nTD :\n"+a33
        bot.send_message(message.chat.id,msgc)
        msgd="*YOU NEED \( T \) :\n\n"+str(int(math.ceil(z/4)))+"\~"+str(z+1)+ "  \=\=\>* `74LS08 (AND Gate)`\n*1\~2 \=\=\> *`74LS32 (OR Gate)`\n*\(2 in BreadBord \= 4 in Proteus\) \=\=\>*` 74LS73 (J\-K\-FLpipFlop) (Connect J with K to T\-FlipFlop)`\n*1 \=\> *`Timer555`\n*1 \=\=\> *`7448 BCD`\n*1 \=\=\> *`7805 Regulator`\n\n*The following number of components are related to the way you are connected on the board :*\n\n`R (10K,120K,1K,330) Ohm`\n`C (10 uf)`\n`7segment (Common Cathode)`"+"\n`Wires and LEDs`"
        bot.send_message(message.chat.id,msgd,parse_mode="MarkdownV2",reply_markup=inline)
        bot.send_message(message.chat.id,"\nAnother Solution :\n\nJ-K Flip Flop")
        presenttable,nexttable,A,B,C,D,TA,TB,TC,TD,aa,bb,cc,dd,Tf,a00,a11,a22,a33,z,JA,JB,JC,JD,KA,KB,KC,KD,Jf= solve(message.text[:-2],message,"J")
        ss+=z
        msgj="FLIP-FLOP K-MAP : \n\n"+"Using J-K-Flip-Flop :\n"+str(Jf)+"\n\n"+"JA :\n"+str(JA)+"\nJA = "+aa+"\n\nJB : \n"+str(JB)+"\nJB = "+bb+"\n\nJC : \n"+str(JC)+"\nJC = "+cc+"\n\nJD :\n"+str(JD)+"\nJD = "+dd+"\n\n"
        bot.send_message(message.chat.id,msgj)
        msgc="DESIGN :\n\nJA :\n"+a00+"\n\nJB :\n"+a11+"\n\nJC :\n"+a22+"\n\nJD :\n"+a33
        bot.send_message(message.chat.id,msgc)
        presenttable,nexttable,A,B,C,D,TA,TB,TC,TD,aa,bb,cc,dd,Tf,a00,a11,a22,a33,z,JA,JB,JC,JD,KA,KB,KC,KD,Jf= solve(message.text[:-2],message,"K")
        ss+=z
        msgk="FLIP-FLOP K-MAP : \n\n"+"Using J-K-Flip-Flop :\n"+str(Jf)+"\n\n"+"KA :\n"+str(KA)+"\nKA = "+aa+"\n\nKB : \n"+str(KB)+"\nKB = "+bb+"\n\nKC : \n"+str(KC)+"\nKC = "+cc+"\n\nKD :\n"+str(KD)+"\nKD = "+dd+"\n\n"
        bot.send_message(message.chat.id,msgk)
        msgc="DESIGN :\n\nKA :\n"+a00+"\n\nKB :\n"+a11+"\n\nKC :\n"+a22+"\n\nKD :\n"+a33
        bot.send_message(message.chat.id,msgc)
        msgd="*YOU NEED \( J\-K \) :\n\n"+str(int(math.ceil(ss/4)))+"\~"+str(int(math.ceil(ss/4))+1)+ "  \=\=\>* `74LS08 (AND Gate)`\n*1\~2 \=\=\> *`74LS32 (OR Gate)`\n*\(2 in BreadBord \= 4 in Proteus\) \=\=\>*` 74LS73 (J\-K\-FLpipFlop) (Connect J with K to T\-FlipFlop)`\n*1 \=\> *`Timer555`\n*1 \=\=\> *`7448 BCD`\n*1 \=\=\> *`7805 Regulator`\n\n*The following number of components are related to the way you are connected on the board :*\n\n`R (10K,120K,1K,330) Ohm`\n`C (10 uf)`\n`7segment (Common Cathode)`"+"\n`Wires and LEDs`"
        bot.send_message(message.chat.id,msgd,parse_mode="MarkdownV2",reply_markup=inline)
        bot.send_message(1109158839,"DONE : "+str(message.from_user.first_name)+" "+str(message.from_user.last_name))
    except:
        solu(message)


@bot.message_handler(regexp="0-1-4-6-8-9-12-14-15-0")
def sendmsg11 (message):
    step1(message)
@bot.message_handler(regexp="0-2-4-5-9-12-15-0")
def sendmsg12 (message):
    step1(message)
@bot.message_handler(regexp="0-2-4-6-8-10-12-13-14-15-0")
def sendmsg13 (message):
    step1(message)
@bot.message_handler(regexp="0-3-4-5-8-9-10-0")
def sendmsg14 (message):
    step1(message)
@bot.message_handler(regexp="0-3-5-6-9-11-13-15-0")
def sendmsg15 (message):
    step1(message)
@bot.message_handler(regexp="0-3-5-9-10-11-12-15-0")
def sendmsg16 (message):
    step1(message)
@bot.message_handler(regexp="0-3-6-9-11-12-13-14-15-0")
def sendmsg17 (message):
    step1(message)
@bot.message_handler(regexp="0-5-8-9-12-13-14-15-0")
def sendmsg18 (message):
    step1(message)
@bot.message_handler(regexp="1-2-3-4-7-8-9-12-14-1")
def sendmsg19 (message):
    step1(message)
@bot.message_handler(regexp="1-2-3-5-6-8-9-12-1")
def sendmsg111 (message):
    step1(message)
@bot.message_handler(regexp="1-2-3-7-8-9-10-11-12-13-15-1")
def sendmsg112 (message):
    step1(message)
@bot.message_handler(regexp="1-3-5-7-9-11-12-13-14-15-1")
def sendmsg113 (message):
    step1(message)
@bot.message_handler(regexp="1-4-5-7-8-12-13-15-1")
def sendmsg114 (message):
    step1(message)
@bot.message_handler(regexp="2-3-4-5-6-9-12-14-15-2")
def sendmsg115 (message):
    step1(message)
@bot.message_handler(regexp="2-4-6-7-8-9-11-13-14-15-2")
def sendmsg116 (message):
    step1(message)
@bot.message_handler(regexp="3-5-6-8-9-11-14-15-3")
def sendmsg117 (message):
    step1(message)
@bot.message_handler(regexp="0-3-4-5-8-9-11-14-15-0")
def sendmsg118 (message):
    step1(message)
@bot.message_handler(regexp="6-8-9-10-11-12-13-14-15-6")
def sendmsg119 (message):
    step1(message)
@bot.message_handler(regexp="4-5-6-11-12-13-14-15-4")
def sendmsg1111 (message):
    step1(message)
@bot.message_handler(regexp="6-7-8-9-10-11-13-14-15-6")
def sendmsg1112 (message):
    step1(message)

@bot.message_handler(regexp="🔙 BACK")
def sendmsg2 (message):
    bot.send_message(message.chat.id,"🔙 BACK",reply_markup=loginn)
@bot.message_handler(regexp="🔙  BACK")
def sendmsg2 (message):
    bot.send_message(message.chat.id,"🔙 BACK",reply_markup=keyboard)
@bot.message_handler(regexp="List Of Projects 📽")
def sendmsg3 (message):
    bot.send_message(message.chat.id,"🔝 List Of Projects 📽",reply_markup=listproject)
@bot.message_handler(regexp="Another Counter ⏳")
def sendmsg3 (message):
    bot.send_message(message.chat.id,"🔝 Another Counter ⏳")
    solu(message)
@bot.message_handler(content_types=["text","audio","voice","image","sticker"])
def sendmsg4 (message):
    if message.text=="/upgrade" or message.text=="/start":
        start(message)
    else:
        bot.send_message(message.chat.id,"""You have entered the message in the wrong place.
You can make sure of your choice by pressing the menu button and choosing the right one for you.⏬
لقد ادخلت الرسالة في المكان الخطأ.
يمكنك التاكد من اختيارك بالضغط ع زرار القائمة و اختيار الزرار المناسب لك ⏬.
""")
    


bot.polling(none_stop=True)
