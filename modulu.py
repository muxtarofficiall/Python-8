def samitler(cumle):
    list=["A","I","O","U","E"]
    newlist=[]
    for i in cumle: 
        a=False
        for j in list:
            if i.upper()==j.upper():
                a=True
                break
        if a==False:
            if i in newlist:
                pass
            elif i==" ":
                pass
            else:
                newlist.append(i)
    
    return newlist
