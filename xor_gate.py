import numpy as np

#*********************************Neuron***************************************
def neuron(x, w, b):
    r=np.sum(np.dot(x,w))+b
    if r>=0:
        return 1
    else:
        return 0

#************************************AND***************************************
def and_perceptron(x):
    w=1
    b=-1.5
    return neuron(x,w,b)

#************************************OR*****************************************
def or_perceptron(x):
    w=1
    b=-1
    return neuron(x,w,b)

#************************************NOT***************************************
def not_perceptron(x):
    w=-1
    b=0.5
    return neuron(x,w,b)

#************************************XOR***************************************
def xor_perceptron(value):
    """ xor(a,b)= ab'+a'b
    xor is (or(a,b))and(nand(a,b))
    """
    y_or=or_perceptron(value)
    y_nand=not_perceptron(and_perceptron(value))
    X5= np.array([y_nand,y_or])
    y_xor=and_perceptron(X5)

    return y_xor

#************************************MAIN***************************************
def main():
    X1=np.array([0,0])
    X2=np.array([0,1])
    X3=np.array([1,0])
    X4=np.array([1,1])
    x_list=[]
    x_list.append(X1)
    x_list.append(X2)
    x_list.append(X3)
    x_list.append(X4)
    for x in x_list:
        print(f"{x[0]} xor {x[1]} is {xor_perceptron(x)}")

if __name__=="__main__":
    main()