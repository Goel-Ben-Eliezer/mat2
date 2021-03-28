a = open("C:\\Users\\User\\Desktop\\mat\\mat2\\text.txt")
a = a.read()
a=a.splitlines()
word = a[0]
a[0]=" "


def revword(w):
    c=''.join(reversed(w))
    c=c.lower()
    #mm=c.split(' ')
    return c


def countword(a):
    i=0
    count=1
    while i < len(a):
        j=0
        s=revword(a[i]).split(' ')
        while j<len(s): 
            if word in s[j]:
                count=count+1
            j=j+1
        i=i+1
    return count
                
    
    
    
    
    
    
    
    
    
    
    



