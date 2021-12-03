def checkSyn(sys1,sys2,dict):
    if dict[sys1]==sys2:
        return True
    else:
        if dict[sys1] in dict.keys():
            return checkSyn(dict[sys1],sys2,dict)
        else:
            return False

with open('example.in','r') as rd:
    synlines = rd.readlines()
    testCases = synlines[0]
    nextLine = 1
    outstr = ''
    with open('out.txt','w') as wr:
        for i in range(int(testCases)):
            dictCount = int(synlines[nextLine])
            nextLine +=1
            dict = {}
            for di in range(int(dictCount)):
                line = synlines[nextLine+di].split()
                dict[line[0]]= line[1]
            testCount = int(synlines[nextLine+dictCount])
            nextLine+=dictCount+1
            for ti in range(int(testCount)):
                line = synlines[nextLine+ti].split()
                sys1 = line[0]
                sys2 = line[1]
                if sys1 in dict.keys():
                    if checkSyn(sys1,sys2,dict):
                        outstr+='synonyms \n'
                    else:
                        outstr+='different \n'
                elif sys2 in dict.keys():
                    checkSyn(sys2,sys1,dict)
                    if checkSyn(sys2,sys1,dict):
                        outstr+='synonyms \n'
                    else:
                        outstr+='different \n'
                elif sys1.lower() == sys2.lower():
                    outstr+='synonyms \n'
                else:
                    outstr+='different \n'
            nextLine +=testCount
        wr.writelines(outstr)