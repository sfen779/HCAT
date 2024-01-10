def readresult(p):
    #print(1)
    #return the x,y,w,h in a string format
    '''
    return the x,y,w,h in a string format
    '''
    result = []
    f = open(p,"r")
    lines = f.readlines()
    for line in lines:
        #print("line is :",line)
        tmp = line.strip().split(",") 
        result.append(tmp)
    return(result)

if "__name__" == "__main__":
    x = readresult("/home/fengshuo/code/HCAT/results/LaSOT/HCAT/dog-1.txt")
    print(x)