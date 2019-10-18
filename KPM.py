def getNext(p:str,next:[] )->[] :
    pLen=p.__len__();
    i=0;
    j=-1;
    next[0]=-1;
    while(i<pLen-1) :
        if j==-1 or p[i]==p[j] :
            i+=1;
            j+=1;
            # if p[i]!=p[j] :
            #     next[i]=j;
            # else :
            #     next[i]=next[j];
            next[i]=j;
        else :
            j=next[j];
    return next;

def KPM(s:str,p:str) ->int:
    i=0;
    j=0;
    sLen=s.__len__();
    pLen=p.__len__();
    nextArr=[0]*pLen;
    next=getNext(p,nextArr);

    while(i<sLen and j<pLen) :
        if s[i]==p[j] or j==-1 :
            i+=1;
            j+=1;
        else :
            j=next[j];
        if j==pLen :
            return i-j;
        

val=KPM("aadgegeyjh","dgedg");
print(val.__str__());