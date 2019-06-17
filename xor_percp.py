def map(ip):
    count=0
    for x in ip:
        if x=='1':
            count+=1
    if count%2==0:
        return 0
    else:
        return 1

def activation_fn(ip,w):
    y=ip*w
    if y>0:
        return 1
    elif y<=0:
        return 0

x="10010111"
w=map(x)
y=activation_fn(int(x),w)
print(y)

