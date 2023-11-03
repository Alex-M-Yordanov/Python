inp=input()
n,m=inp.split(' ')
n=int(n)
m=int(m)
dash='-'
fig='.|.'
string="WELCOME"
fc=1
str=""
for i in range(1,n+1):
        if i==int(n/2)+1:
            for j in range(int((m-len(string))/2)):
                str=str+dash
            str=str+string
            for j in range(int((m-len(string))/2)):
                str=str+dash     
        elif i<int(n/2)+1:
                for j in range(int((m-fc*len(fig))/2)):
                    str=str+dash
                for j in range(fc):
                    str=str+fig
                for j in range(int((m-fc*len(fig))/2)):
                    str=str+dash
                fc=fc+2
        elif i>int(n/2)+1:
                fc=fc-2
                for j in range(int((m-fc*len(fig))/2)):
                    str=str+dash
                for j in range(fc):
                    str=str+fig
                for j in range(int((m-fc*len(fig))/2)):
                    str=str+dash
        print(str)
        str=""
