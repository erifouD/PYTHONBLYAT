a=[i for i in open('список.txt')]
c=''
for i in range(0,len(a)+1):
        l=a.count(a[i])
        if l>1 and c.count(str(a[i]))==0:
            print('элементы',a[i],'повторяются')
            c=c+str(a[i])
      
        
    
    
    
