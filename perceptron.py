f=open("ANDgate.csv","r")
print(f.read())
def Predict():
    alpha=0.9
    output=0
    for row in dataset:
        Expected=row[-1]
        flag=True
        while(flag==True):
            flag=False
            Predicted=weights[0]*row[0]+weights[1]*row[1]
            if Predicted >=theta:
               # print("Activated")
                output=1
            else:
                #print ("Not Activated")
                output=0
            error=Expected-output
            if error!=0:
                weights[0]=weights[0]+alpha*(Expected-output) * row[0]
                weights[1]=weights[1]+alpha*(Expected-output)* row[1]
                flag=True
            else:
                flag=False    
    print("The new value of new weight1 is",weights[0],"The new value of new weights2",weights[1])            
dataset=[[0,0,0],[0,1,0],[1,0,0],[1,1,1]]
weights=[0.5,0.5]
theta=1
Predict()
    ##print("Expected=%d, Predicted=%d" % (row[-1], Predict))
    
    
