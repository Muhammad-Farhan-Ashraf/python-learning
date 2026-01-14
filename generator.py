def Square():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1
num=Square()
for i in num:
    print(i)