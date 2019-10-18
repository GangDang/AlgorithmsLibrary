def manacher(s:str):
    #将被填充的新字符串
    newStr=[];
    #新字符串长度
    newStrLen=len(s)*2+1;
    #字符串填充特殊字符
    for item in s :
        newStr.append('#');
        newStr.append(item);
    newStr.append('#');

    print(newStr);

    #右方边界，初始为0
    rightBoundary=0;
    #中心标志位，初始为0
    centerTag=0;
    #存放新字符串内部存在的回文字符串半径
    p=[0]*newStrLen;

    for i in range(newStrLen):
        #i点以centerTag为中心的对称点
        j=centerTag*2-i;
        #在指定范围内右边回文字符串的半径
        rightRound=rightBoundary-i;
        #大于等于零表示 i点在指定范围内
        if rightRound>0:
            #表示右边的字回文字符串在指定范围内
            if j<rightRound:
                p[i]=p[j];
            else:
                p[i]=rightRound;
                while p[i]<newStrLen-i and newStr[i-p[i]]==newStr[i+p[i]]:
                    p[i]+=1;
                #移动对称中心
                centerTag=i;
                #扩大范围边界
                rightBoundary=i+p[i];
        else:
            p[i]=1;
            while p[i]<newStrLen-i and newStr[i-p[i]]==newStr[i+p[i]]:
                p[i]+=1;
            centerTag=i
            rightBoundary=i+p[i];
    print(p);


manacher("hsysurwdfhrtjuet");
    

