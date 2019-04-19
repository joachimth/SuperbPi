with open('test.csv','a') as file:
    i = 0
    while(i<10):
        i+=1
        file.write('\n%d,%d'%(i,i*2))
