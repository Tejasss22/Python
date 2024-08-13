def countt(String,substring,truth_value) :
    count = 0;
    length = len(substring);
    if(truth_value) :
        for i in range(0,len(String)):
            s = String[i:i+length];
            if(s == substring):
                count+=1;
    else:
    	String.count(substring);
    return count;
print(countt("sgsgsgsg","sgs",True))
